# 泊松过程

$\renewcommand{\geq}{\geqslant}\renewcommand{\leq}{\leqslant}$
满足如下条件的随机过程$\{N(t), t\geq 0\}$为**时齐泊松过程**。

1. $\{N(t), t\geq 0\}$为计数过程，且$N(0) = 0$；
2. $\{N(t), t\geq 0\}$为独立增量过程；
3. $\{N(t), t\geq 0\}$具备增量平稳性，即$N(t) - N(s)$的分布仅与$t - s$有关
4. 对于充分小的$\Delta t > 0$，有

    $$
    \left\{
    \begin{aligned}
        P(N(t + \Delta t) - N(t) = 1) &= \lambda \Delta t + o(\Delta t) \\
        P(N(t + \Delta t) - N(t) \geq 2) &= o(\Delta t)
    \end{aligned}
    \right.
    $$

## 增量的概率分布

泊松过程的增量$N(t + s) - N(s)$服从参数为$\lambda t$的泊松分布，即

$$
P[N(t + s) - N(s) = k] = \frac{(\lambda t)^k}{k!}e^{-\lambda t}
$$

???+ proof "证明"

    根据泊松过程的增量平稳性，