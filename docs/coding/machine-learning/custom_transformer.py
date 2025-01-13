import torch

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
        Q = self.W_Q(x_q).reshape(N, L_Q, self.num_heads, self.d_k)
        K = self.W_K(x_k).reshape(N, L_KV, self.num_heads, self.d_k)
        V = self.W_V(x_v).reshape(N, L_KV, self.num_heads, self.d_k)

        score = torch.einsum('nihd,njhd->nijh', Q, K) / self.sqrt_d_k
        # score: (N, L_Q, L_KV, num_heads)
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
        return super().forward(x, x, x, padding_mask, attention_mask)


class MultiHeadCrossAttention(MultiHeadAttention):
    def __init__(self, d_model: int, num_heads: int):
        super(MultiHeadCrossAttention, self).__init__(d_model, num_heads)

    def forward(
        self, x_q: torch.Tensor, x_kv: torch.Tensor,
        padding_mask: torch.Tensor | None = None,
        attention_mask: torch.Tensor | None = None
    ) -> torch.Tensor:
        return super().forward(x_q, x_kv, x_kv, padding_mask, attention_mask)

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
