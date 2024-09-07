# 激活函数

激活函数是神经网络中用于引入非线性因素的函数。常用的激活函数有如下几种：

## Sigmoid 函数

Sigmoid函数是一个将输入值压缩到0到1之间的函数，常用$\sigma$表示。Sigmoid函数常用于二分类问题中，将输出值映射到概率空间。

$$
\begin{aligned}
\sigma(x) &= \frac{1}{1 + e^{-x}} \\
\sigma'(x) &= \sigma(x)(1 - \sigma(x))
\end{aligned}
$$

```python
def sigmoid(x: torch.Tensor) -> torch.Tensor:
    return 1 / (1 + torch.exp(-x))

class Sigmoid(torch.nn.Module):
    def __init__(self):
        super(Sigmoid, self).__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return sigmoid(x)
```

## Softmax 函数

Softmax函数是一个将输入值压缩到0到1之间的函数，常用于多分类问题中，将多个分类上输出值映射到概率空间，所有类别的概率之和为1。

$$
\begin{aligned}
\text{softmax}(\bsz)_i &= \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}} \\
\text{softmax}'(\bsz)_i &= \text{softmax}(\bsz)_i(1 - \text{softmax}(\bsz)_i)
\end{aligned}
$$

```python
def softmax(x: torch.Tensor, dim: int = -1) -> torch.Tensor:
    return torch.exp(x) / torch.exp(x).sum(dim=dim, keepdim=True)

class Softmax(torch.nn.Module):
    def __init__(self, dim: int = -1):
        super(Softmax, self).__init__()
        self.dim = dim

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return softmax(x, dim=self.dim)
```

相对应的，softmin函数是softmax函数的对称函数，用于最小化输出值，$\text{softmin}(\bsz) = \text{softmax}(-\bsz)$。
