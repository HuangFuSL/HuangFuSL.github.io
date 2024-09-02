# 注意力机制

## 序列建模

语言模型是一类序列模型，其目标是对给定的序列建模，即对序列中的每个位置预测下一个位置的概率。文本首先通过分词，获得对应的离散符号（token），然后经过嵌入层（embedding layer）将符号映射到$D$维向量空间。因此，序列建模的输入是一个$N\times L\times D$的张量，其中$N$是batch size，$L$是序列长度，$D$是嵌入维度。

## Transformer

Transformer由Vaswani等人在2017年提出，其核心思想是注意力机制，即通过查询、键的匹配得分为值分配权重，从而实现对序列的建模。注意力机制的数学表达为：

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{\bsQ\bsK^\top}{\sqrt{d_k}}\right)\bsV
$$

自注意力机制指的是查询、键和值都来自同一个序列。在实现中，输入序列$\bsx$分别经过三组线性变换$\bsW^Q, \bsW^K, \bsW^V$得到查询$\bsQ$、键$\bsK$和值$\bsV$，然后计算注意力得分，最后通过值的加权求和得到输出。交叉注意力机制指查询和

!!! note "为什么需要线性变换"
    线性变换的目的是将输入序列映射到不同的语义空间，另外一方面也使得注意力机制不再受到矩阵对称的约束（A对B的注意力可以不等于B对A的注意力）。

!!! note "为什么要除以$\sqrt{d_k}$"
    在$\bsQ\bsK^\top$的计算中，结果的方差会发生变化，为了使结果的方差保持不变，需要除以$\sqrt{d_k}$，其中$d_k$是键的维度。否则，当$d_k$较大时，$\bsQ\bsK^\top$中元素之间的差异会变得很大，导致softmax函数的梯度接近于0。

!!! note "softmax函数"
    softmax函数的定义为：

    $$
    \text{softmax}(\bsz)_i = \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}}
    $$

    即对输入向量$\bsz$中每个元素指数的归一化。其中$\bsz$是输入向量，$n$是向量的维度。

为了从多个维度学习到对同一个位置不同特征的表征，transformer引入了多头注意力机制。其核心思想是将输入的$D$维向量拆分到$h$个头，然后分别计算注意力，最后将$h$个头的输出拼接在一起，再经过一个线性变换得到最终输出。在实现中，一般使用维度变换来实现输入向量的拆分。

在部分任务中，需要控制序列某个位置的元素只能依赖于该位置之前的元素，而不能依赖于之后的元素。此时需要使用mask机制，即在计算注意力得分时，将不合法的位置的得分设置为负无穷，从而在softmax函数中得到0的概率。

## 代码实现

!!! note "einsum"
    `einsum`是Einstein Summation Notation的缩写，是一种用于张量运算的记号。在PyTorch中，`einsum`函数的定义为：

    ```python
    torch.einsum(equation, *operands)
    ```

    其中`equation`是一个字符串，描述了张量的运算方式，`operands`是一个或多个张量。例如，`torch.einsum("ij,jk->ik", A, B)`表示计算矩阵$A$和$B$的乘积。可以将其理解为乘积-求和的过程，即将`equation`中的字母对应到`operands`中的张量，然后对这些张量进行乘积和求和。忽略batch size，我们需要计算$\bsQ\bsK^\top$，其中$\bsQ$的维度是$(L, D)$，$\bsK$的维度是$(L, D)$，输出的维度是$(L, L)$，因此`equation`为`"id,jd->ij"`。

下面我们通过PyTorch实现多头注意力机制。在实现注意力机制前，需要先实现线性变换和softmax函数。之后实现用于多头注意力的`MultiHeadSelfAttention`类，其输入是一个$N\times L\times D$的张量，输出是一个$N\times L\times D$的张量。

```python
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadAttention, self).__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")

        self.d_k = d_model // num_heads
        self.sqrt_d_k = self.d_k ** 0.5

        self.W_Q = torch.nn.Linear(d_model, d_model)
        self.W_K = torch.nn.Linear(d_model, d_model)
        self.W_V = torch.nn.Linear(d_model, d_model)
        self.W_O = torch.nn.Linear(d_model, d_model)

    def forward(
        self, x_q: torch.Tensor, x_k: torch.Tensor, x_v: torch.Tensor,
        mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        N, L_Q, D = x_q.size()
        _, L_KV, _ = x_k.size()
        Q = self.W_Q(x_q).reshape(N, L_Q, self.num_heads, self.d_k)
        K = self.W_K(x_k).reshape(N, L_KV, self.num_heads, self.d_k)
        V = self.W_V(x_v).reshape(N, L_KV, self.num_heads, self.d_k)

        score = torch.einsum("nihd,njhd->nijh", Q, K) / self.sqrt_d_k
        score = torch.nn.functional.softmax(score, dim=2)
        value = torch.einsum("nijh,njhd->nihd", score, V).reshape(N, L_Q, self.d_model)
        return self.W_O(value)

class MultiHeadSelfAttention(MultiHeadAttention):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadSelfAttention, self).__init__(d_model, num_heads)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        return super().forward(x, x, x, mask)

class MultiHeadCrossAttention(MultiHeadAttention):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadCrossAttention, self).__init__(d_model, num_heads)

    def forward(
        self, x_q: torch.Tensor, x_kv: torch.Tensor,
        mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        return super().forward(x_q, x_kv, x_kv, mask)
```

!!! note "注意力机制中的mask"

    在实现中，有时需要对注意力机制的得分进行mask操作，以控制模型的行为。mask通常分为三种，即

    1. padding mask：维度`[N, L]`，用于掩盖序列中的padding元素，使其不参与注意力计算。
    2. attention mask：维度`[L, L]`，用于自注意力机制中，控制序列中元素的依赖关系。通常用causal mask或look-ahead mask规定序列某个位置的元素只能依赖于该位置之前的元素，而不能依赖于之后的元素。
    3. 在交叉注意力机制中的memory mask：维度`[L_Q, L_KV]`，用于控制查询和键之间的依赖关系。

    在实现中，我们可以将mask中为0的元素设置为负无穷，从而在softmax函数中得到0的概率。

完整的多头注意力机制实现如下

```python
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadAttention, self).__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")

        self.d_k = d_model // num_heads
        self.sqrt_d_k = self.d_k ** 0.5

        self.W_Q = torch.nn.Linear(d_model, d_model)
        self.W_K = torch.nn.Linear(d_model, d_model)
        self.W_V = torch.nn.Linear(d_model, d_model)
        self.W_O = torch.nn.Linear(d_model, d_model)

    def forward(
        self, x_q: torch.Tensor, x_k: torch.Tensor, x_v: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        attention_mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        # x_q: (N, L_Q, D), x_k: (N, L_KV, D), x_v: (N, L_KV, D)
        # padding_mask: (N, L_KV), attention_mask: (L_Q, L_KV)
        N, L_Q, D = x_q.size()
        _, L_KV, _ = x_k.size()

        # Linear transformation -> Split heads
        Q = self.W_Q(x_q).reshape(N, L_Q, self.num_heads, self.d_k)
        K = self.W_K(x_k).reshape(N, L_KV, self.num_heads, self.d_k)
        V = self.W_V(x_v).reshape(N, L_KV, self.num_heads, self.d_k)

        # Compute attention score
        score = torch.einsum('nihd,njhd->nijh', Q, K) / self.sqrt_d_k

        # Apply attention mask
        if attention_mask is not None:
            score = score.masked_fill(
                attention_mask.reshape(1, L_Q, L_KV, 1) == 0, float('-inf')
            )

        # Apply padding mask
        if padding_mask is not None:
            score = score.masked_fill(
                padding_mask.reshape(N, 1, L_KV, 1) == 0, float('-inf')
            )

        # Softmax -> Weighted sum -> Merge heads -> Output transformation
        score = torch.nn.functional.softmax(score, dim=2)
        value = torch.einsum(
            'nijh,njhd->nihd', score, V
        ).reshape(N, L_Q, self.d_model)
        return self.W_O(value)


class MultiHeadSelfAttention(MultiHeadAttention):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadSelfAttention, self).__init__(d_model, num_heads)

    def forward(
        self, x: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        attention_mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        # Self attention is applied to the same input
        return super().forward(x, x, x, padding_mask, attention_mask)


class MultiHeadCrossAttention(MultiHeadAttention):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadCrossAttention, self).__init__(d_model, num_heads)

    def forward(
        self, x_q: torch.Tensor, x_kv: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        attention_mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        # Cross attention is applying query on another kv sequence
        return super().forward(x_q, x_kv, x_kv, padding_mask, attention_mask)
```