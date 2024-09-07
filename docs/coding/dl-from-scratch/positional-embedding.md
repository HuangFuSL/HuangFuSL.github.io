# 位置编码

Attention机制虽然能捕捉序列中不同位置的依赖关系，但是无法区分不同位置的元素。为了解决这个问题，Transformer模型引入了位置编码（Positional Encoding）。

## 绝对位置编码

绝对位置编码是Transformer模型中最早引入的位置编码方式，其核心思想是为序列中的每个位置分配一个唯一的向量，将这个向量和输入序列相加得到最终序列的表示。如BERT模型，限制了序列的最大长度为512，因此可以使用固定的位置编码，将每个位置映射到一个可学习的向量。

```python
class AbsolutePE(torch.nn.Module):
    def __init__(self, max_len: int, d_model: int):
        super(AbsolutePE, self).__init__()
        self.pe = torch.nn.Embedding(max_len, d_model)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [N, L]
        pos = torch.arange(x.size(1), device=x.device).unsqueeze(0)
        return self.pe(pos) # [1, L, D], can be broadcasted to [N, L, D]
```

此类方法的缺点是无法处理超过最大长度的序列，并且忽视了元素之间的相对位置关系。

## 正弦位置编码

Vaswani等人提出的位置编码包含一个正弦函数和一个余弦函数，其数学表达为：

$$
\begin{aligned}
PE_{(pos, 2i)} &= \sin(pos / 10000^{2i / d_{\text{model}}}) \\
PE_{(pos, 2i + 1)} &= \cos(pos / 10000^{2i / d_{\text{model}}}) \\
\end{aligned}
$$

其中，$pos$表示位置，$i$表示维度，$d_{\text{model}}$表示模型的维度，输出的位置编码直接与输入序列相加得到最终表示。正弦位置编码不需要额外进行学习。Vaswani的实验表明，固定的位置编码和可学习的位置编码在性能上没有显著差异。

```python
class SinusoidPE(torch.nn.Module):
    def __init__(self, d_model: int):
        super(SinusoidPE, self).__init__()
        self.d_model = d_model

    def _denominator(self, device: torch.device) -> torch.Tensor:
        return 10000 ** (torch.arange(0, self.d_model, device=device) / self.d_model)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [N, L]
        pos = torch.arange(x.size(1), device=x.device).unsqueeze(0) # [1, L]
        pos = pos.unsqueeze(-1) / self._denominator(x.device) # [1, L, D]
        pos[:, :, 0::2] = torch.sin(pos[:, :, 0::2])
        pos[:, :, 1::2] = torch.cos(pos[:, :, 1::2])
        return pos # [1, L, D], can be broadcasted to [N, L, D]
```

## 旋转位置编码

Su等人提出的[旋转位置编码](https://arxiv.org/abs/2104.09864)（Rotary Positional Embedding，RoPE）。编码的核心思想是通过旋转矩阵将位置信息嵌入到特征空间中，从而使模型能够学习到位置信息。

$$
f_{q, k} \bsx_m = \bsR_{\Theta, m}^d W_{q, k} \bsx_m
$$

其中，$\bsR_{\Theta, m}$为旋转矩阵，将向量每两个分量进行旋转。

$$
\begin{aligned}
\bsR^k_{\Theta, m} &= \begin{bmatrix}
\cos(m\theta_k) & -\sin(m\theta_k) \\
\sin(m\theta_k) & \cos(m\theta_k)
\end{bmatrix} \\
\bsR_{\Theta, m} &= \begin{bmatrix}
\bsR^1_{\Theta, m} & 0 & \cdots & 0 \\
0 & \bsR^2_{\Theta, m} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \bsR^{d / 2}_{\Theta, m}
\end{bmatrix}_{d\times d}
\end{aligned}
$$

注意，$m$为位置，取值范围为$1, \ldots, L$，$k$为维度下标，取值范围为$1, \ldots, d / 2$。最终的旋转操作将每个位置$m$的向量$\bsx_m$应用旋转矩阵$\bsR_{\Theta, m}$，得到新的向量。

```python
import functools

class RoPE(torch.nn.Module):
    def __init__(self, d_model: int, theta: int | float = 10000):
        super(RoPE, self).__init__()
        self.d_model = d_model
        self.theta = theta ** -(torch.arange(0, d_model, 2) / d_model)

    @functools.lru_cache(maxsize=None)
    def _forward_l(self, L: int) -> torch.Tensor:
        # Use lru_cache to avoid redundant computation for the same L

        D = self.d_model
        pos = torch.einsum(
            'l,d->ld',
            torch.arange(L), self.theta
        )  # [L, D / 2]

        # Major diagonal is cos, cos, ..., cos; D elements
        cos = torch.cos(pos).repeat_interleave(2)
        # Minor diagonal is sin, 0, sin, 0, ..., sin; D - 1 elements
        sin = torch.stack([
            torch.sin(pos), torch.zeros_like(pos), dim=-1
        ]).reshape(L, D)[:, :-1]

        result = torch.zeros(L, D, D)
        result = torch.diagonal_scatter(result, cos, dim1=1, dim2=2)
        result = torch.diagonal_scatter(result, sin, dim1=1, dim2=2, offset=-1)
        result = torch.diagonal_scatter(result, -sin, dim1=1, dim2=2, offset=1)
        return result

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [N, L, H, D]
        _, L, _, D = x.size()
        rot_matrix = self._forward_l(L).to(x.device)  # [L, D, D]
        return torch.einsum('lde,nlhe->nlhd', rot_matrix, x)
```

和其他位置编码方式不同，RoPE在QKV变换后进行位置编码，因此需要对注意力机制的实现进行修改。

```python hl_lines="2 5 16-22"
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int, num_heads: int, rope: RoPE | None = None):
        ...

        self.rope = rope

        ...

    def forward(
        self, x_q: torch.Tensor, x_k: torch.Tensor, x_v: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        attention_mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        ...

        if self.rope is not None:
            Q = self.rope(self.W_Q(x_q).reshape(N, L_Q, self.num_heads, self.d_k))
            K = self.rope(self.W_K(x_k).reshape(N, L_KV, self.num_heads, self.d_k))
        else:
            Q = self.W_Q(x_q).reshape(N, L_Q, self.num_heads, self.d_k)
            K = self.W_K(x_k).reshape(N, L_KV, self.num_heads, self.d_k)
        V = self.W_V(x_v).reshape(N, L_KV, self.num_heads, self.d_k)

        ...
```

为了计算方便，[Llama](llama-2.ipynb/#_2)等部分模型的RoPE将输入向量分为前后两段，前后两段相同位置的元素分为一组进行旋转操作，而不是将整个向量按照相邻的两个元素分为一组进行旋转。
