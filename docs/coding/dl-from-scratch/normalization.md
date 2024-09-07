# 归一化

归一化是指将数据按照比例缩放，改变其分布。按照归一化的维度不同，可以分为以下几种：

* **样本归一化（Batch Normalization）**：对每个特征进行归一化，通常用于图像数据$B \times C \times H \times W$，在同一$C$维度上计算均值和方差。
* **层归一化（Layer Normalization）**：对每个样本进行归一化，通常用于序列数据$B\times L \times D$，在同一$B$维度上计算均值和方差。
* **实例归一化（Instance Normalization）**：对每个样本的每个特征维度进行归一化，在同一$B\times C$维度上计算均值和方差。
* **分组归一化（Group Normalization）**：对每个样本中的特征分成若干组后，在同一组内进行归一化。

归一化的方式为

$$
x' = \frac{x - \mu}{\sigma} \times \gamma + \beta
$$

其中$\mu, \sigma$分别为样本均值和标准差，$\gamma, \beta$为可学习的重缩放参数。给定特征维度$d$，归一化层的参数量为$2d$。

## RMSNorm

Zhang等人在LN的基础上提出了RMSNorm，相比于LN，RMSNorm不需要计算均值和方差，而是直接使用均方根作为归一化的标准，并且在重缩放阶段删去了偏置$\beta$。

$$
x' = \frac{x}{\sqrt{\frac{1}{N} \sum_{i=1}^{N} x_i^2}} \times \gamma
$$

```python
class RMSNorm(torch.nn.Module):
    def __init__(self, dim: int, eps=1e-8):
        super(RMSNorm, self).__init__()
        self.gamma = torch.nn.Parameter(torch.ones(dim))
        self.eps = eps

    def forward(self, x: torch.Tensor):
        return x / torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + self.eps) * self.gamma
```
