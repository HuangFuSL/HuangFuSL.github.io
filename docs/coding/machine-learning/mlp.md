# 多层感知机

多层感知机（Multilayer Perceptron, MLP）是深度学习的基础，也是最简单的深度学习模型之一，由线性变换和非线性的[激活函数](activation.md)组成。多层感知机的网络结构是由输入层、多个隐藏层和输出层组成，其中隐藏层的神经元数量和层数可以自由设定。

## 线性变换

线性变换是多层感知机的基础，它是由输入层到隐藏层和输出层的全连接层组成。线性变换的数学表达式为：

$$
y = Wx + b
$$

其中 $W$ 是权重矩阵，$x$ 是输入向量，$b$ 是偏置向量，$y$ 是输出向量。

```python
class Linear(torch.nn.Module):
    def __init__(self, in_dim: int, out_dim: int):
        super(Linear, self).__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.weight = torch.nn.Parameter(torch.randn(out_dim, in_dim))
        self.bias = torch.nn.Parameter(torch.randn(out_dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.einsum("ij,j->i", self.weight, x) + self.bias
```

反向传播中，梯度计算公式为：

$$
\begin{aligned}
\frac{\partial y}{\partial W} &= x \\
\frac{\partial y}{\partial b} &= 1
\end{aligned}
$$
