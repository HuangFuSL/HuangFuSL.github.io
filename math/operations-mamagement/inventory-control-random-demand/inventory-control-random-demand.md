# 随机需求下的库存控制

优化目标：最小化成本的数学期望

## 单周期——报童模型

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
    C(Q) &= E(G(Q, D) | Q) \\
    &= \int_{0}^\infty G(Q, D)f(x)\mathrm dx \\
    &= \int_{0}^Q c_o(Q-x)f(x)\mathrm dx + \int_Q^\infty c_u(x-Q)f(x)\mathrm dx \\
\end{aligned}
$$

当$C(Q)$取极小值时，有$\frac{\mathrm dC}{\mathrm dD} = 0$，即

$$
\begin{aligned}
    \frac{\mathrm dC}{\mathrm dQ} &= c_o\int_0^Q f(x)\mathrm dx + c_u\int_Q^\infty -f(x)\mathrm dx \\
    &= c_oF(Q) - c_u(1-F(Q)) \\
    &= 0
\end{aligned}
$$

验证：$\frac{\mathrm d^2 C}{\mathrm dQ^2} = (c_o + c_u)f(Q) > 0$，因此为极小值点。此时$F(Q^*) = c_u / (c_o + c_u)$。

称$c_u / (c_o + c_u)$为**关键比例**（crucial ratio）

### 单周期模型扩展

#### 离散需求的最优策略

确定$\max_{Q_0}, \min_{Q_1}$满足$Q_1 > Q_0$且$F(Q_0) < c_u / (c_u + c_o) < F(Q_1)$，此时$Q_1$即为最优的$Q^*$。即高于最优关键比例的最小关键比例对应的$Q$

#### 存在初始库存$u$

$u$的存在不影响$Q^*$，因此，订货量$Q'$满足

$$
Q^{*\prime} = \max\{Q^*-u, 0\}
$$

## 周期检查模型

在周期检查模型中，首先不考虑固定订货成本$K$的影响。需求分为多个周期，每个周期的需求独立同分布。

### 记号

* 剩余周期数为$n$
* 每个周期的需求独立同分布，需求的概率密度函数为$f(\cdot)$，概率分布函数为$F(\cdot)$。
* 周期之间的贴现率$\alpha$表示
* 不考虑订货提前期，$L=0$
* $y_i$表示第$i$期结束时的库存，$y_0$表示期初库存
* $C_n(y_0)$表示第$n$期总期望贴现成本的最小值

$$
C_n(y_0) = \min_{y\geq y_0}\left\{L(y) - cy_0 + \alpha\int_{0}^\infty C_{n-1}[t(y, x)]f(x)\mathrm dx\right\}
$$