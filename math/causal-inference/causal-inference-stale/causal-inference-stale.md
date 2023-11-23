# 因果推断

> Casual inference is about studying the consequence of doing one thing vs another.

!!! theorem "Simpson’s Paradox"

    某个统计关联，可能在所有子群体上的效果都是相反的。

    > A statistical association that holds for the entire population can be
    > reversed in every subpopulation.

    {{ latex_image('imgs/casual-inference-1.tex') }}

!!! theorem "Berkson’s Paradox"

    > Variables that have no relationships can appear to have strong
    > associations in a selected subpopulation.

因果推断有两个主要的研究框架，即 Potential outcome framework 和 Causal graph 。

## Potential Outcome Framework

### 框架设定

* Unit of analysis：不同时间下的同一个个体应当看作不同的个体
* Treatment $D$：通常划分为实验组（$D=1$）与对照组（$D=0$），但$D$也可以取多值或连续
* Potential outcome $Y(d)$：当干预水平为$d$时**应当**出现的结果。
* Counterfactual outcome：当干预水平为$D$时所有$d\not = D$的结果——存在但无法观测到
* Casual effect：比较两个平行结果之间的差异，$Y(1) - Y(0)$

当一个个体接收到$d=D$之后，其干预状态就不会再改变。因此不可能观测到一个个体所有可能出现的干预结果。

!!! theorem "SUTVA assumption"

    假设个体$i$的干预状态$D_i$、干预和不干预的效果$Y_i(0), Y_i(1)$独立同分布，即

    $$
    \{D_i, Y_i(0), Y_i(1)\}\sim\{D, Y(0), Y(1)\}
    $$

    同时假设

    1. 每个个体的结果不受到其他个体干预水平的影响（不存在个体之间的相互影响，个体的结果只受干预水平的影响）
    2. 不存在干预水平的隐藏状态（即，每个干预状态都是原子的，不可以进一步划分）

考虑总体的期望干预效果（ Average Treatment Effect, ATE）

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

当$Y, D$满足

$$
(Y(0), Y(1))\perp D
\label{1}
$$

时，有$\hat\tau = \tau$

### 混淆因子

!!! theorem ""

    考虑如下场景：

    1. 一群被试随机接受药物试验
    2. 被试中症状比较严重的个体接受药物实验

1. 随机试验指分配机制由研究者可控。如按照$p = 0.5$的概率进行伯努利实验随机分配，则$(Y(1)， Y(0))\perp D$，此时有$\hat\tau = \tau$
2. 观测研究指分配机制不由研究者控制。如被试根据个体感受自行决定吃药。此时存在（可以观测到的）混淆因子$X$

!!! definition "混淆因子"

    变量$X$是混淆因子，如果：

    1. $X$会影响分配，即$X\not \perp D$，或
    2. $X$会影响结果，即$X\not \perp (Y(1)， Y(0))$

    通常将可观测到的混淆因子记为$X$，不能观测到的混淆因子记为$U$。

因此，当存在混淆因子时，$\eqref{1}$不再成立，其中的$D$变为$D|X$

当所有的混淆因子都被观测到，则可以适用 unconfoundedness assumption

!!! theorem "Unconfoundedness assumption"

    假设成立时，有

    $$
    (Y(1), Y(0)) \perp D|X
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

但实际上，不可能观测到所有的混淆因子。此时

$$
\begin{aligned}
    & \bbE [Y | D = 1] - \bbE [Y| D = 0] \\
    =& \bbE[\bbE[Y | D = 1, X] | D = 1] - \bbE[\bbE[Y | D = 0, X] | D = 0]
\end{aligned}
$$

但实际上，$\bbP(X|D = 1) \not = \bbP(X|D = 0)$，因此造成偏差。

!!! theorem "干预与条件"

   * $\bbE(Y|D = 0)$反映条件，作用在群体$D = 0$上。
   * $\bbE(Y(0))$反映干预，作用在全体上。

当$(Y(1), Y(0))\perp D | X$成立时，有

$$
\bbE(Y(1) | X) = \bbE(Y | D = 1, X)
$$

前提是， overlap assumption 成立。

!!! definition "Overlap assumption"

    对于所有的$X$，$Y(0), Y(1)$必须都存在，即

    $$
    \bbP(D=1|X)\in (0, 1)
    $$

    定义$\bbP(D=1|X)\in (0, 1)$为propensity score。

### 实证研究

实际上， unconfoundedness 和 overlap 假设均不一定成立，因为有许多隐藏的混淆因子。

对于前文中的 Simpson’s Paradox ，出现反直觉现象的原因在于，性别是一个混淆因子：

1. 女性的被试比例更高（$D\not\perp X$）
2. 女性整体的康复率更低（$Y\not\perp X$）

在实证研究中，往往还有研究者未能观测到的混淆因子。

混淆因子既是障碍，也是工具。在理想化的统计推断中，相关性不能推出因果性。但在实证研究中，由于混淆因子的存在，使得我们可以区分相关性中的因果关系。

!!! theorem "一些衡量干预效果的指标（参数）"

    ATE

    $$
    \tau = \bbE[Y(1) - Y(0)]
    $$

    被试的 ATE

    $$
    \tau_1 = \bbE[Y(1) - Y(0) | D = 1]
    $$

    条件 ATE（ CATE ）

    $$
    \tau_C = \bbE[Y(1) - Y(0) | (D, X)\in \text{subgroup}]
    $$

    QTE（ Quantile treatment effect ）

    $$
    \begin{gathered}
        \text{QTE} = F_1^{-1}(\gamma) - F_0^{-1}(\gamma) \\
        F_d^{-1}(\gamma) = \inf\{y|\bbP(Y(d)\leq y)\geq \gamma\}
    \end{gathered}
    $$

    Causal risk ratio（只适用于结果二分的情况）

    $$
    \text{CRR} = \bbP(Y(1) = 1) / \bbP(Y(0) = 1)
    $$

以上这些参数都受到混淆变量（不一定能被观测到）的影响。相对应的，从实验结果的统计指标中，我们可以得到这些指标的一个估计。

如对于 ATE 指标$\tau = \bbE[Y(1) - Y(0)]$，$\tilde \tau = \bbE[Y | D = 1] - \bbE[Y | D = 0]$就是$\tau$的一个估计。

$\tau$是一个因果参数，受到$X, D, Y(0), Y(1)$的共同影响。$\tilde\tau$是一个可以从统计数据中观测到的指标，受到$X, D, Y$的共同影响。

如果某个参数，可以从统计数据中观测到一个唯一的无偏估计，则称为 identifiable 。由于反事实的存在，我们只能观测到$Y = Y(D)$，因此即使有无限多的数据集，也不一定能实现 identification 。在 unconfoundedness 假设成立的条件下，可以实现 identification 。

因此，为了验证一个因果关系是否成立，我们需要两方面的信息

1. 充足的数据集以反映$X, D, Y$的分布。
2. 关于$X, D, Y(0), Y(1)$的一些假设，如随机试验假设或 unconfoundedness 假设。

## Causal Graph

一系列变量的因果关系可以构成因果图。因果图是一个有向无环图（ DAG ），其中的节点表示变量，每条边从父变量（节点）出发，指向子变量（节点）。

* 相邻：如果两个节点之间有一条边，称两个节点**相邻**
* （因果）路径：一系列相邻的节点组成一条**路径**（无视边的方向）
* 有向路径：**方向相同**的一系列路径所连接的节点形成的路径

路径有如下形式：

* 链：$A\ra B\ra C$
* 汇聚：$A\ra B\la C$
* 分支：$A\la B\ra C$

在因果图中，每个节点都是其子节点（后代）的直接原因（祖先）（即，不存在中间的变量影响子节点）。

对于如下图所示的因果图

{{ latex_image('imgs/casual-inference-2.tex') }}

1. $X_1$影响变量$X_4$，但不是直接影响。
2. 如果固定$X_3$，则$X_1$的变化不会影响$X_4$，即

    $$
    X_4\perp (X_1, X_2) | X_3
    $$

3. 但$X_4$仍然与$X_5$有关。

进一步地，我们不妨假设，如果控制了某个变量$X_i$全部的直接祖先，则$X_i$只与其后代有关（因果Markov假设）。

!!! theorem "Markov因子分解"

    当Markov假设成立时，对于$n$个变量$X_1, \ldots, X_n$，有

    $$
    \bbP(X_1, \ldots, X_n) = \prod_{i=1}^n \bbP(X_i | A_i)
    $$

    式中，$A_i$为$X_i$全部的祖先。

### d-分割

对于有两个节点的因果图，$X_1\la X_2$和$X_1\ra X_2$是两个不同的因果关系，但在相关性上有相同的表现，无法区分。

对于有三个节点的因果图：

* $X_1\ra X_2\ra X_3$和$X_1\la X_2\ra X_3$是两个不同的因果关系，但它们都满足$X_1\perp X_3 | X_2, X_1\not\perp X_3$，仍然无法区分。并且由于变量$X_2$的存在，即使$X_1, X_3$存在相关关系，也不能说明其存在直接或间接的因果关系。控制$X_2$可以**阻断**$X_1, X_3$的因果链。
* 对于$\X_1\ra X_2\la X_3$，如果控制$X_2$，则有$X_1\not \perp X_3 | X_2$，但$X_1\perp X_3$。$X_2$**阻断了**$X_1, X_3$的因果链。
    * 如果有另一个变量$X_4$满足$X_2\ra X_4$，则控制$X_4$也会使$X_1, X_3$表现出相关，即$X_1\not \perp X_3 | X_4$。

!!! theorem "阻断因果链"

    两个变量之间的路径如果满足下列之一，则因果关系不能通过这条路径（被阻断）。

    1. 存在一个没有被控制的汇聚节点；
    2. 存在一个被控制的非汇聚节点。

    如果两个变量之间的所有路径都被阻断，则这两个变量被分割。

一般定义被控制的变量集合为$Z$。如果因果图$\calG$中，控制变量$Z$将因果图分为了两个部分，则这两个部分$X, Y$构成了因果图的一个d-分割，即$X\perp_\calG Y | Z$。进一步地，如果满足 Markov 假设，则$X$中的所有变量和$Y$中的所有变量独立。

但是变量独立不一定能导出d-分割，由此得到 faithfulness assumption

!!! theorem "faithfulness assumption"

    对于因果图$\calG$，若对于任意互不相交的$X, Y, Z$且$X\perp Y | Z$，则$X, Y$构成一个d-分割。

在 Markov 假设和 faithfulness 假设成立的情况下，d-分割等价于变量独立。

### 相关性与因果性的路径

在因果图上：

* 相关性沿路径流动
* 因果性沿有向路径流动

如果阻断了所有非因果性的路径，则两个变量之间存在因果关系。

!!! definition "do算子"

    在因果图中，对一个变量的干预可以通过阻断所有指向该变量的边实现，记作$\mathrm {do}(\cdot)$

非因果的路径有两个来源：

* 没有控制分支变量，即 confounding bias
* 控制了汇聚变量，即 selection bias

#### Confounding 与后门调整

Confounding 指因果路径的起始和终结变量都受到同一个混淆因子的影响。可以通过后门调整消除影响。
