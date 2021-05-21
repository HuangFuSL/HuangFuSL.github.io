# 目标规划

目标规划解决现实生活中的多目标决策问题。

设线性规划$(P)$：

$$
\begin{aligned}
    & \max z=c^Tx \\
    & s.t. \left\{
    \begin{aligned}
        & AX \leq b \\
        & X\geq 0
    \end{aligned}
    \right .
\end{aligned}
$$

假设优化问题的目标调整为：

> 寻找使得$z\geq z_0$的$X$，其中$z_0$为指定的目标。允许$z > z_0$但不允许$z < z_0$

此时的优化问题即为目标规划，引入两个松弛变量$d^+, d^-$，分别表示目标函数超出目标值的部分与不足目标值的部分，为保证目标函数超过目标值，可以按照如下方式建模：

$$
\begin{aligned}
    & \max w = d^- \\
    & s.t. \left\{
    \begin{aligned}
        & c^Tx - d^+ + d^- = z_0 \\
        & AX \leq b \\
        & X\geq 0
    \end{aligned}
    \right .
\end{aligned}
$$

由此可见，目标规划相当于在线性规划中引入一种新的约束条件，即目标约束。每个目标约束都需要引入一对变量$d^+$与$d^-$。如果优化问题中存在多个目标且之间存在优先级关系，可以使用$P_i$作为需要优化的目标函数系数。$P_i$满足$P_1 \gg P_2 \gg \dots \gg P_n$并且各$P_i$为足够大的正数。