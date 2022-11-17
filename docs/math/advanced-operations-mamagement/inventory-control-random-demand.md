# 随机需求下的库存控制

优化目标：最小化成本的数学期望

## 报童模型

报童模型是单周期下的库存控制问题

### 记号

* $c_o$表示超额订货成本，$c_u$表示缺货成本
* $f(\cdot), F(\cdot)$分别为需求的概率密度函数与概率分布函数
* $Q$为订货量
* $x^+ = \max\{x, 0\}$

### 推导

报童模型的成本函数为

$$
G(Q, D) = c_o\max\{0, Q-D\} + c_u\max\{0, D-Q\}
$$

$G(Q, D)$是随机变量$D$的函数，因此也是随机变量，对$D$取期望，有

$$
\begin{aligned}
    G(Q) &= E(G(Q, D)) \\
    &= \int_{0}^\infty G(Q, D)f(x)\mathrm dx \\
    &= \int_{0}^Q c_o(Q-x)f(x)\mathrm dx + \int_Q^\infty c_u(x-Q)f(x)\mathrm dx \\
\end{aligned}
$$

当$G(Q)$取极小值时，有$\frac{\mathrm dG}{\mathrm dD} = 0$，即

$$
\begin{aligned}
    \frac{\mathrm dG}{\mathrm dQ} &= c_o\int_0^Q f(x)\mathrm dx + c_u\int_Q^\infty -f(x)\mathrm dx \\
    &= c_oF(Q) - c_u(1-F(Q)) \\
    &= 0
\end{aligned}
$$

验证：$\frac{\mathrm d^2 G}{\mathrm dQ^2} = (c_o + c_u)f(Q) > 0$，因此为极小值点。此时$F(Q^*) = c_u / (c_o + c_u)$。

称$c_u / (c_o + c_u)$为**关键比例**（crucial ratio）

### 模型扩展

#### 离散需求的最优策略

确定$\max_{Q_0}, \min_{Q_1}$满足$Q_1 > Q_0$且$F(Q_0) < c_u / (c_u + c_o) < F(Q_1)$，此时$Q_1$即为最优的$Q^*$

#### 存在初始库存$u$

$u$的存在不影响$Q^*$，因此，订货量$Q'$满足

$$
Q^{*\prime} = \max\{Q^*-u, 0\}
$$