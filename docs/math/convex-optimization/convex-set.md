# 凸集

从直观意义上讲，凸集就是没有凹进去的部分的集合。

## 定义

### 直线

设$x_1 \not = x_2$为$\mathbb R^n$上的两个点，则

* $y = \theta x_1 + (1 - \theta) x_2$ 定义了一条**直线**。
* $y = \theta x_1 + (1 - \theta) x_2, 0\leq\theta\leq 1$ 定义了一条**线段**。

直线$y = \theta x_1 + (1 - \theta) x_2$是一条从$x_2$出发，沿向量$x_1 - x_2$方向延伸的直线。

### 仿射集合

对于$\mathbb R^n$中的$m$个点$x_1, \ldots, x_m$，若$\sum_{i = 1}^m \theta_i = 1$，则称$\sum_{i=1}^m \theta_ix_i$为$x_1, \ldots, x_m$的**仿射组合**。

如果一组向量$x_1, \ldots, x_m$中的每一个向量都不能由其他向量经仿射组合得到，称这组向量**仿射无关**。

???+ theorem "仿射无关与线性无关"

    一组向量$x_0, x_1, \ldots, x_m$仿射无（相）关等价于向量$x_1 - x_0, \ldots, x_m - x_0$线性无（相）关。

设集合$C \subseteq \mathbb R^n$，若集合$C$中的任意两个不同点构成的直线（即它们的仿射组合）仍然位于集合中，则$C$为**仿射集合**。

$$
\forall x_1, x_2 \in C, x_1 \not = x_2, \forall \theta\in \mathbb R, y = \theta x_1 + (1 - \theta) x_2\in C
$$

仿射集合$C$满足如下性质

* $C$中包含其中任意个点的仿射组合。
* 集合$V = \{x - x_0 | x \in C\}$为$\mathbb R^n$的子空间，且其维数与偏移$x_0$无关。定义仿射集合的维数为$V$的维数。

设$C$为任意集合，则$C$中所有点的仿射组合称为$C$的**仿射包**，记作$\mathbf{aff} C$，仿射包是包含集合$C$的最小（即维数最低的）仿射集合，其维数称为**仿射维数**。

当一个集合$C$的仿射维数$\dim \mathbf{aff} C < n$时，$C^\circ = \varnothing$。此时需要定义相对内部与相对边界。

* 集合$C$的**相对内部**定义为$\mathbf{relint}C = \{x\in C | \exists r\in \mathbb R_{ + + }, B(x, r)\cap \mathbf{aff} C \subseteq C\}$
* 集合$C$的**相对边界**定义为$\mathbf{cl} C - \mathbf{relint}C$。

### 凸集

对于集合$C\subseteq \mathbb R^n$中的$m$个点$x_1, \ldots, x_m$，若$\sum_{i=1}^m \theta_i = 1, \theta_i \geq 0$，则称$\sum_{i=1}^m \theta_i x_i$为$x_1, \ldots, x_m$的**凸组合**。

若一个集合内任意两点的凸组合都在该集合中，称该集合为**凸集**。

$$
\forall x_1, x_2\in C, \forall 0\leq \theta\leq 1, \theta x_1 + (1 - \theta) x_2\in C
$$

集合$C$的所有点的凸组合称为**凸包**，记作$\mathbf{conv}C$，$C$的凸包是包含$C$的最小凸集。

### 锥

对于集合$C$，若$\forall x\in C, \forall \theta\geq 0, \theta x\in C$，则称$C$为**锥**。若$C$还是凸集，则称为**凸锥**。凸锥满足

$$
\forall x_1, x_2\in C, \forall \theta_1, \theta_2 \geq 0, \theta_1x_1 + \theta_2x_2 \in C
$$

对于集合$C\subseteq \mathbb R^n$中的$m$个点$x_1, \ldots, x_m$，若$\theta_i \geq 0$，则称$\sum_{i=1}^m \theta_i x_i$为$x_1, \ldots, x_m$的**锥组合**。

集合$C$中所有元素组成的所有锥组合称为**锥包**，$C$的锥包是包含$C$的最小凸锥。

## 常见的凸集

以下是一些平凡凸集：

* 空集$\varnothing$、单点集$\{x_0\}$、全空间$\mathbb R^n$及其子空间都是仿射集（也是凸集）。
* 任意直线都是凸集；过原点的直线是仿射集；线段是凸集；射线是凸集；起点在原点的射线是凸锥。

### 超平面与半空间

设$a\in \mathbb R^n, a \not = 0, b\in \mathbb R$，方程$a^\top x = b$确定了线性空间$\mathbb R^n$内的一个**超平面**，这个超平面将空间分为两部分，称为**开半空间**，每一部分加上超平面称为**半空间**。

* 超平面可以表示为$\{x | a^\top x = b\}$
* 半空间可以表示为$\{x | a^\top x\leq b\}$

向量$a$为超平面的法线方向，超平面上的所有点都可以由一个起点$x_0$加上与$a$正交的所有向量得到。

### 球

$\mathbb R^n$中的**欧氏球**为2-范数下的球，即

$$
B(x, r) = \{y | \Vert y - x\Vert_2\leq r\}
$$

其中$x\in \mathbb R^n$为欧氏球的球心，$r\in \mathbb R_{++}$为其半径。

**椭球**是各个方向延伸程度不同的欧氏球，延伸程度由矩阵$P\in \mathbb S_{++}$确定，半轴长度为$\sqrt{\lambda_i}$。

$$
\mathcal E = \{y | (x - y)^\top P^{-1}(x - y)\leq 1\}
$$

当$P = r^2I$时，$\mathcal E = B(x, r)$。

将欧氏球中的2-范数换成其他的范数，就可以得到**范数球**：

$$
B_*(x, r) = \{y | \Vert y - x\Vert_* \leq r\}
$$

### 锥

方程$\Vert x\Vert_2 \leq t$在$R^{n+1}$上定义了一个**锥**，称为**二阶锥**。锥可以视为由低一维的球堆积得到。

将2-范数替换为其他范数可以得到**范数锥**。

### 多面体

有限个线性等式和不等式的解集构成**多面体**。

$$
\begin{aligned}
    \mathcal P &= \{x | a_i^\top x\leq b_i, i = 1, \ldots, m, c_j^\top x = d_j, j = 1, \ldots, p\} \\
    &= \{x | Ax\preceq b, Cx = d\}
\end{aligned}
$$

多面体可以是锥，如非负象限。

单纯形是一种特殊的多面体，一组仿射无关的点$x_0, x_1, \ldots, x_m$的凸组合确定了一个**单纯形**，用$\mathbf{conv}\{x_0, \ldots, x_m\}$表示，其仿射维度为$m$。

$$
\mathbf{conv}\{x_0, \ldots, x_m\} = \left\{\theta_0x_0 + \theta_1x_1 + \cdots + \theta_mx_m \middle| \theta_i \geq 0, \sum_{i=1}^m \theta_i = 1\right\}
$$

* **单位单纯形**是零向量和单位向量确定的$n$维单纯形，即$\{x | x\geq 0, \mathbf{1}^\top x \leq 1\}$。
* **概率单纯形**是单位向量确定的$n-1$维单纯形，即$\{x | \mathbf 1^\top x = 1\}$。

???+ theorem "单纯形与多面体"

    单纯形是一种特殊的多面体。设单纯形$C$由仿射无关的向量$x_0, \ldots, x_m$确定，则

    $$
    B = \begin{bmatrix}
        x_1 - x_0 & \cdots & x_m - x_0
    \end{bmatrix}
    $$

    $B$是一个$n\times m$维的满秩矩阵。令$\theta = \begin{pmatrix}\theta_0 & \theta_1 & \cdots & \theta_m\end{pmatrix}, \theta' = \begin{pmatrix}\theta_1 & \cdots & \theta_m\end{pmatrix}$。当空间中的一个点$x$满足$x\in C$时，有

    $$
    \exists \theta\succeq 0, \mathbf 1^\top \theta = 1, x = \sum_{i=0}^m \theta_i x_i \Longleftrightarrow \exists \theta'\succeq 0, \mathbf 1^\top \theta' \leq 1, x = x_0 + B\theta'
    $$

    而$B$是满秩矩阵，则存在满秩矩阵$A$使得

    $$
    AB = \begin{bmatrix}
        A_1 \\ A_2
    \end{bmatrix}B = \begin{bmatrix}
        I \\ 0
    \end{bmatrix}
    $$

    则

    $$
    Ax = \begin{bmatrix}
        A_1 \\ A_2
    \end{bmatrix}x = \begin{bmatrix}
        A_1x \\ A_2x
    \end{bmatrix} = \begin{bmatrix}
        A_1x_0 + \theta' \\ A_2x_0
    \end{bmatrix}
    $$

    该单纯形的多面体表示为：

    $$
    C = \{x | A_1x\succeq A_1x_0, A_2x = A_2x_0, \mathbf 1^\top A_1x - \mathbf 1^\top A_1x_0\leq 1\}
    $$

### 半正定锥

设$\mathbb S^n_{+}$表示全体$n$阶对称半正定矩阵的集合，则$\mathbb S^n_+$是一个凸锥。（注意此处对锥的理解和范数锥不同）。

$$
A\succeq 0, B\succeq 0\Longrightarrow x^\top (\theta_1 A + \theta_2 B)x \geq 0\Longrightarrow (\theta_1A + \theta_2B)\succeq 0
$$

## 保凸运算

保凸运算是在运算前后保持集合凸性的运算。

1. 部分和$\{(x, y_1 + y_2) | (x, y_1) \in A, (x, y_2)\in B\}$，有两种极端情况
   1. $\dim y_1 = \dim y_2 = 0$时退化为交运算$\cap$：一个凸集可以表示为一系列半空间的交集。
   2. $\dim x = 0$时退化为和$+: A + B = \{x + y | x\in A, y\in B\}$。
2. 线性变换$f: \mathbb R^n\rightarrow \mathbb R^m = Ax + b$。
3. 直积$\times, A\times B = \{(x, y) | x\in A, y\in B\}$。
4. 投影函数$P: \mathbb R^n\times \mathbb R_{++}\rightarrow \mathbb R^n$，$P(z, t) = z / t$。投影函数将$\mathbb R^{n}\times \mathbb R_{++}$空间中的点投影到平面$x_{n+1} = 1$上。
5. 线性变换和投影函数的组合，称为线性分式函数。

## 广义不等式

定义**正常锥**为满足如下条件的锥：

* 是凸锥。
* 是闭集（存在边界）
* 存在内部。
* 不包含直线（$x\in K, -x\in K\Longleftrightarrow x = 0$）

正常锥$K$可以在空间$\mathbb R^n$上定义广义不等式：

$$
\begin{gathered}
    x \preceq_K y \triangleq y - x\in K \\
    x \prec_K y \triangleq y - x\in K^\circ
\end{gathered}
$$

* 若$K = \mathbb R_+$，广义不等式等价于实数域上的不等式。
* 若$K = \mathbb R^n_+$，广义不等式等价于$\mathbb R^n$空间中向量的分量不等式。
* 若$K = \mathbb S^n_+$，广义不等式等价于矩阵不等式。

广义不等式满足如下性质

* $x\preceq_K y, u\preceq_K v\Longrightarrow x + u\preceq_K y + v$，对$\prec_K$也成立。
* $x\preceq_K y, y\preceq_K z\Longrightarrow x\preceq_K z$，对$\prec_K$也成立。
* $x\preceq_K y, \alpha\geq 0\Longrightarrow \alpha x\preceq_K \alpha y$，当$\alpha > 0$时对$\prec_K$也成立。
* $x\prec_K y\Longrightarrow x\preceq_K y$
* $x\preceq_K x, x\not\prec_K x$
* $x\preceq_K y, y\preceq_K x\Longrightarrow x = y$
* $\forall i\in \mathbb N, x_i\preceq_K y_i, \lim_{i\rightarrow\infty} x_i = x, \lim_{i\rightarrow\infty} y_i = y\Longrightarrow x\preceq_K y$
* $x\preceq_K y\Longrightarrow \exists u, \exists v, x + u\prec_K y+ v$

广义不等式不是线性的，即$\exists x, \exists y, x\not \preceq_K y, y\not \preceq_K x$，此时称$x, y$不可比。

定义了偏序关系后就可以在此基础上定义极小值与最小值。

* $x\in S$是**最小元**当且仅当$S\subseteq \{y | y\succeq_K x\}$，即$S$中元素全部与$x$可比且大于等于$x$。
* $x\in S$是**极小元**当且仅当$S\cap \{y | y\preceq_K x\} = \{x\}$，即$S$中不存在和$x$可比且比$x$更小的元素。

## 超平面与凸集

### 分离超平面

给定凸集$A, B$满足$A\cap B = \varnothing$，则存在$a\in \mathbb R^n, b\in \mathbb R, a\not = 0$使得

$$
\forall x\in A, \forall y\in B, a^\top x - b\leq 0, a^\top y - b\geq 0
$$

称$\{x | a^\top x = b\}$为集合$A, B$的**分离超平面**。

若超平面$\{x | a^\top x = b\}$满足

$$
\forall x\in A, \forall y\in B, a^\top x - b < 0, a^\top y - b > 0
$$

称$\{x | a^\top x = b\}$严格分离$A, B$，严格分离的超平面不一定存在。

???+ theorem "不存在严格分离的例子"

    设集合$A = \{(x, y) | xy\geq 1\}, B = \{(x, y) | x\leq 0, y\leq 0\}$，则集合$A, B$被超平面$\{(x, y) | x = 0\}$和$\{(x, y) | y = 0\}$分离，但不存在严格分离两个集合的超平面。

    {{ latex_image('imgs/strict-separation.tex', 'strict-separation') }}

    同理，$\{(x, y) | y\leq \ln x\}$和$\{(x, y) | x\leq 0\}$之间也不存在严格分离的超平面

超平面分离的逆定理不成立。

### 支撑超平面

设集合$C\subseteq \mathbb R^n$，对于$x_0\in \partial C$，若存在$a\not = 0$满足

$$
\forall x\in C, a^\top x\leq a^\top x_0
$$

称$\{x| a^\top x = a^\top x_0\}$为$C$在$x_0$处的**支撑超平面**。对于边界上的某个点，支撑超平面不一定唯一。

若集合$C$是凸集，则其边界上所有点都存在一个支撑超平面。给定$C$是闭集且$C^\circ\not =\varnothing$，则逆定理也成立。

## 对偶锥

给定锥$K$，若$K^*$满足

$$
y\in K^* \Longleftrightarrow \forall x\in K, x^\top y\geq 0
$$

称$K^*$为$K$的**对偶锥**。对偶锥必定是凸锥。

???+ proof "对偶锥的凸性"

    给定锥$K$，有$\forall x\in K, \forall \theta\geq 0, \theta x \in K$，则对于任意$y\in K^*$

    $$
    \theta x^\top y = x^\top (\theta y)\geq 0\Longrightarrow \theta y\in K^*
    $$

    因此$K^*$是锥。设$y_1, y_2\in K^*, x\in K, 0\leq \theta\leq 1$，则

    $$
    x^\top (\theta y_1)\geq 0, x^\top(1 - \theta)y_2\geq 0\Longrightarrow x^\top (\theta y_1 + (1 - \theta)y_2)\geq 0
    $$

    因此$K^*$是凸的。

对偶锥可能和原锥相等，如$\mathbb R^n_{+}, \mathbb S^n_{+}$的对偶分别是其本身。

* $K^*$是闭凸锥。
* $K_1\subseteq K_2\Longrightarrow K_2^*\subseteq K_1^*$
* 若$K^\circ\not = \varnothing$，则$K^*$是尖的。
* 若$\mathbf{cl}K$是尖的，则$(K^*)^\circ\not = \varnothing$
* $K^{**} = \mathbf{cl}K$

对于正常锥$K$，存在一个对偶锥$K^*$，两者都能用于定义广义不等式$\preceq_K$，称$\preceq_{K^*}$为$\preceq_K$的对偶。

广义不等式的对偶$\preceq_{K^*}$满足

* $x\preceq_K y\Longleftrightarrow \forall \lambda\succeq_{K^*}0, \lambda^\top x\leq \lambda^\top y$
* $x\prec_K y\Longleftrightarrow \forall \lambda\succeq_{K^*}0, \lambda\not = 0, \lambda^\top x < \lambda^\top y$

对于集合$S$中的元素$x\in S$：

* $x$关于$\preceq_K$是最小元等价于$\forall \lambda \succeq_{K^\ast}0$，$x$是极小化$\lambda^\top z, z\in S$的唯一最优解，即$\forall \lambda \succeq_{K^\ast}0, \{z | \lambda^\top x = \lambda^\top z\}$是一个严格支撑超平面。
* 若$x$关于$\preceq_K$是极小元，则存在$\lambda\succ_{K^*} 0$，$\forall z\in S, \lambda^\top z\geq \lambda^\top x$，也即存在一个严格支撑超平面。当$S$为凸集时，逆定理对于存在$\lambda\succeq_{K^*}0$成立。