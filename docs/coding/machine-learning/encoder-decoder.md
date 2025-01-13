# 编码器与解码器

在[注意力机制](attention.md)的基础上，Vaswani等人提出了两种transformer架构，即编码器和解码器。编码器利用自注意力机制，对输入的序列进行编码，解码器则利用自注意力机制和交叉注意力机制，生成对序列中下一个元素的预测。

## 编码器

编码器由多个相同的层组成，每个层包含一个残差连接的多头自注意力机制和一个前馈神经网络。在残差连接前，使用dropout；在残差连接后，使用层归一化来防止过拟合。前馈神经网络由两个全连接层组成，两个全连接层之间通常使用ReLU或GeLU等激活函数。

```python
ACT2FN = {
    'relu': torch.nn.ReLU,
    'gelu': torch.nn.GELU,
}

class FFN(torch.nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, activation: str = 'relu'):
        super(FFN, self).__init__()
        self.fc1 = torch.nn.Linear(input_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, input_dim)
        self.act = ACT2FN[activation]()

    def forward(self, x):
        return self.fc2(self.act(self.fc1(x)))


class EncoderLayer(torch.nn.Module):
    def __init__(
        self, input_dim: int, num_heads: int,
        ffn_dim: int | None = None, dropout: float = 0.1,
        layer_norm_eps: float = 1e-6, activation: str = 'relu'
    ):
        super(EncoderLayer, self).__init__()

        if ffn_dim is None:
            ffn_dim = input_dim * 4

        self.attention = MultiHeadSelfAttention(input_dim, num_heads)
        self.norm1 = torch.nn.LayerNorm(input_dim, layer_norm_eps)
        self.dropout1 = torch.nn.Dropout(dropout)

        self.ffn = FFN(input_dim, ffn_dim, activation)
        self.norm2 = torch.nn.LayerNorm(input_dim, layer_norm_eps)
        self.dropout2 = torch.nn.Dropout(dropout)

    def forward(
        self, x, padding_mask: torch.Tensor | None = None,
        src_mask: torch.Tensor | None = None
    ):
        x = x + self.dropout1(self.attention(x, padding_mask, src_mask))
        x = self.norm1(x)

        x = x + self.dropout2(self.ffn(x))
        x = self.norm2(x)

        return x


class Encoder(torch.nn.Module):
    def __init__(
        self, num_layers: int, input_dim: int, num_heads: int,
        ffn_dim: int | None = None, dropout: float = 0.1,
        layer_norm_eps: float = 1e-6, activation: str = 'relu'
    ):
        super(Encoder, self).__init__()

        self.layers = torch.nn.ModuleList([
            EncoderLayer(
                input_dim, num_heads, ffn_dim,
                dropout, layer_norm_eps, activation
            )
            for _ in range(num_layers)
        ])

    def forward(
        self, x, padding_mask: torch.Tensor | None = None,
        src_mask: torch.Tensor | None = None
    ):
        # x: (N, L, D)
        if src_mask is None:
            src_mask = torch.ones(x.size(1), x.size(1)).to(x.device)
        for layer in self.layers:
            x = layer(x, padding_mask, src_mask)
        return x
```

## 解码器

解码器在编码器的基础上，将自注意力机制由双向改为单向，并且在自注意力层和前馈神经网络层之间增加了一个残差连接的多头交叉注意力机制。交叉注意力机制使用编码器的输出作为全局键和值，解码器自注意力层的输出作为查询。在残差连接前后使用dropout和层归一化。注意对于decoder-only的transformer，没有交叉注意力层，而是仅包含一个单向自注意力层。

```python
class DecoderLayer(torch.nn.Module):
    def __init__(
        self, input_dim: int, num_heads: int,
        ffn_dim: int | None = None, dropout: float = 0.1,
        layer_norm_eps: float = 1e-6, activation: str = 'relu'
    ):
        super(DecoderLayer, self).__init__()

        if ffn_dim is None:
            ffn_dim = input_dim * 4

        self.self_attention = MultiHeadSelfAttention(input_dim, num_heads)
        self.norm1 = torch.nn.LayerNorm(input_dim, layer_norm_eps)
        self.dropout1 = torch.nn.Dropout(dropout)

        self.cross_attention = MultiHeadCrossAttention(input_dim, num_heads)
        self.norm2 = torch.nn.LayerNorm(input_dim, layer_norm_eps)
        self.dropout2 = torch.nn.Dropout(dropout)

        self.ffn = FFN(input_dim, ffn_dim, activation)
        self.norm3 = torch.nn.LayerNorm(input_dim, layer_norm_eps)
        self.dropout3 = torch.nn.Dropout(dropout)

    def forward(
        self, x: torch.Tensor, memory: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        memory_mask: torch.Tensor | None = None,
        tgt_mask: torch.Tensor | None = None
    ):
        if tgt_mask is None:
            tgt_mask = torch.triu(
                torch.ones(x.size(1), x.size(1)), diagonal=1
            ).to(x.device)

        x = x + self.dropout1(self.self_attention(x, padding_mask, tgt_mask))
        x = self.norm1(x)

        x = x + self.dropout2(self.cross_attention(x, memory, padding_mask, memory_mask))
        x = self.norm2(x)

        x = x + self.dropout3(self.ffn(x))
        x = self.norm3(x)

        return x


class Decoder(torch.nn.Module):
    def __init__(
        self, num_layers: int, input_dim: int, num_heads: int,
        ffn_dim: int | None = None, dropout: float = 0.1,
        layer_norm_eps: float = 1e-6, activation: str = 'relu'
    ):
        super(Decoder, self).__init__()

        self.layers = torch.nn.ModuleList([
            DecoderLayer(
                input_dim, num_heads, ffn_dim, dropout,
                layer_norm_eps, activation
            )
            for _ in range(num_layers)
        ])

    def forward(
        self, x: torch.Tensor, memory: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        memory_mask: torch.Tensor | None = None,
        tgt_mask: torch.Tensor | None = None
    ):
        # x: (N, L, D)
        for layer in self.layers:
            x = layer(x, memory, padding_mask, memory_mask, tgt_mask)
        return x
```

## transformer的时空复杂度

给定输入序列的长度$L$，输入维度$D$，编码器层数$N$，前馈神经网络的隐藏层维度$D_{ff}$，则transformer的空间复杂度为

* 注意力层：每层包含四个$D \rightarrow D$的全连接层，每个全连接层包含$D \times D + D$个参数（权重+偏置），共$4ND(D + 1)$个参数；
* 前馈神经网络：共$N$层，每层包含一个$D \rightarrow D_{ff}$的全连接层和一个$D_{ff} \rightarrow D$的全连接层，共$2NDD_{ff} + ND_{ff} + ND$个参数；
* 层归一化：每层编码器包含两个归一化，每个归一化包含两个$D$维的缩放参数和偏置参数，共$4ND$个参数。

因此，transformer的总参数量为$4ND(D + 1) + 2NDD_{ff} + ND_{ff} + ND + 2ND$。在Vaswani等人的实现中，$D_{ff} = 4D$，则transformer的参数量为$12ND^2 + 13ND$。解码器比编码器多了一个交叉注意力层（$4ND(D + 1)$）和1个归一化层（$2ND$），因此解码器的参数量为$16ND^2 + 19ND$。

矩阵运算$\bbR^{m\times n}\times \bbR^{n\times p} \rightarrow \bbR^{m\times p}$的时间复杂度为$O(mnp)$，逐步分析transformer的计算过程，忽略加法和归一化的时间复杂度：

1. 线性变换：$\bbR^{L\times D}\times \bbR^{D\times D} \rightarrow \bbR^{L\times D}$，时间复杂度为$O(LD^2)$；
2. 多头注意力：$\bbR^{L\times D}\times \bbR^{D\times L}\rightarrow \bbR^{L\times L}$，时间复杂度为$O(L^2D)$；
3. 前馈神经网络：$\bbR^{L\times D}\times \bbR^{D\times D_{ff}}\rightarrow \bbR^{L\times D_{ff}}$，时间复杂度为$O(LDD_{ff})$。按照$D_{ff} = 4D$，则时间复杂度为$O(4LD^2) = O(LD^2)$。

$D$为常数，模型共叠加$N$层串行计算，因此transformer的时间复杂度为$O(NL^2D)$。