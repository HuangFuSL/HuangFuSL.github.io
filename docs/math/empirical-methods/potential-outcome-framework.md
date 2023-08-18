---
todo: true
---

# Potential Outcome Framework

* Unit of analysis：不同时间下的同一个个体应当看作不同的个体
* Treatment $D$：通常划分为实验组（$D=1$）与对照组（$D=0$），但$D$也可以取多值或连续
* Potential outcome $Y(d)$：当干预水平为$d$时**应当**出现的结果。
* Counterfactual outcome：当干预水平为$D$时所有$d\not = D$的结果——存在但无法观测到
* Casual effect：比较两个平行结果之间的差异，$Y(1) - Y(0)$

假设：

1. 每个个体的结果不受到其他个体干预水平的影响（no interference）
2. 不存在干预水平的隐藏状态

考虑总体的期望干预效果

$$
\tau = \mathbb E[Y(1) - Y(0)]
$$

由于对于个体$i$，无法同时观测$Y_i(1), Y_i(0)$，因此$\tau$的确切数值同样无法观测。

$$
\begin{aligned}
    \hat\tau &= \frac{1}{n_1} \sum_{i;D_i = 1}Y_i - \frac{1}{n_0} \sum_{i;D_i = 0}Y_i \\
    &= \mathbb E[Y(1) | D = 1] - \mathbb E[Y(0) | D = 0]
\end{aligned}
$$

需要考虑$D$的分布，即实验组与对照组如何产生，或$Y, D$的独立性。

!!! theory ""

    考虑如下场景：

    1. 一群被试随机接受药物试验
    2. 被试中症状比较严重的个体接受药物实验

1. 随机试验指分配机制由研究者可控。如按照$p = 0.5$的概率进行伯努利实验随机分配，则$(Y(1)， Y(0))\bot D$，此时有$\hat\tau = \tau$
2. 观测研究指分配机制不由研究者控制。如被试根据个体感受自行决定吃药。此时存在混淆因子$X$
    1. $X$会影响分配，即$X\not \bot D$
    2. $X$会影响结果，即$X\not \bot (Y(1)， Y(0))$

Unconfoundeness假设

$$
(Y(1), Y(0)) \bot D|X
$$

控制混淆因子，此时有

$$\begin{aligned}
    & \mathbb E [\mathbb E[Y | D = 1, X] - \mathbb E[Y | D = 0, X]] \\
    =& \mathbb E [\mathbb E[Y(1) | D = 1, X] - \mathbb E[Y(0) | D = 0, X]] \\
    =& \mathbb E [\mathbb E[Y(1) | X] - \mathbb E[Y(0) | X]] \\
    =& \mathbb E [\mathbb E[Y(1) - Y(0) | X]] \\
    =& \mathbb E[Y(1) - Y(0)]
\end{aligned}
$$