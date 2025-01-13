# 损失函数

损失函数是用来评价模型预测值与真实值之间的差异的函数。然后通过优化算法来调整模型的参数，使得损失函数的值最小。

## 均方误差

均方误差（Mean Squared Error, MSE）是回归任务中最常用的损失函数。它计算的是预测值与真实值之间的平方差的均值。

$$
\begin{aligned}
L(y, t) &= \frac{1}{2} \sum_{i=1}^{n} (y_i - t_i)^2 \\
\frac{\partial L}{\partial y_i} &= y_i - t_i
\end{aligned}
$$

其中，$y$ 是模型的预测值，$t$ 是真实值，$n$ 是样本数量。

```python
def mse(y: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
    return 0.5 * torch.sum((y - t) ** 2)

class MSELoss(torch.nn.Module):
    def __init__(self):
        super(MSELoss, self).__init__()

    def forward(self, y: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        return mse(y, t)
```

## 交叉熵

交叉熵（Cross Entropy）是多分类任务中最常用的损失函数。它计算的是模型输出值与真实值之间的交叉熵，可以通过KL散度推导得到。

$$
\begin{aligned}
KL(p||q) &= -\sum_{i=1}^{n} p_i (\log q_i - \log p_i) \\
&= -\sum_{i=1}^{n} p_i \log q_i + \sum_{i=1}^{n} p_i \log p_i \\
&= H(p, q) - H(p)
\end{aligned}
$$

其中，$p$ 是真实概率分布，$q$ 是模型输出概率分布，$H(p)$表示真实分布$p$的熵，为常数。当输出分布$q$与真实分布$p$相近时，KL散度值越小，交叉熵$-\sum_{i=1}^{n} p_i \log q_i$值也越小。

需要注意的是，在PyTorch中，`torch.nn.CrossEntropyLoss`函数的输入是模型的输出值和真实标签，**不需要**对输出值进行softmax操作。

```python
def cross_entropy(score: torch.Tensor, label: torch.Tensor) -> torch.Tensor:
    # label: [N], score: [N, C]
    score = torch.softmax(score, dim=-1)
    label_logits = score[torch.arange(score.size(0)), label]
    return -torch.sum(torch.log(label_logits))

class CrossEntropyLoss(torch.nn.Module):
    def __init__(self):
        super(CrossEntropyLoss, self).__init__()

    def forward(self, score: torch.Tensor, label: torch.Tensor) -> torch.Tensor:
        return cross_entropy(score, label)
```
