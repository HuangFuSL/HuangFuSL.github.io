# 凸优化问题

优化问题是指在一定的约束条件（等式或不等式）下使目标函数取得最大（最小）值的问题。

## 一般优化问题

$\eqref{1}$定义了一个优化问题。

$$
\label{1}
\optim{\min}{f_0(x)}{\cases{
    \begin{aligned}
    & f_i(x)\leq 0 & i = \oneto m\\
    & h_i(x) = 0 & i = \oneto p
    \end{aligned}
}}
$$

式$\eqref{1}$中，$x\in \bbR^n$为**优化变量**，$f_0(x): \bbR^n \ra \bbR$为**目标函数**，不等式$f_i(x)\leq 0$称为**不等式约束**，$h_0(x) = 0$称为**等式约束**。$m = p = 0$的问题称为**无约束问题**。

目标函数和全体约束函数的定义域交集是优化问题的定义域，当存在$x$满足所有的约束条件时，称优化问题是**可行**的，否则是**不可行**的。定义优化问题的**可行域**为全体可行点的集合。

$$
X = \{x | f_i(x)\leq 0, h_j(x) = 0, i = \oneto m, j = \oneto p\}
$$

对于最小化目标函数的优化问题，其最优值为

$$
p^\ast = \inf\{f_0(x) | x\in X\}
$$

!!! theorem "可行域为空集的情况"

    我们允许$p^*$取$\pm\infty$，并且定义

    $$
    \begin{aligned}
    \inf\varnothing &= \infty \\
    \sup\varnothing &= -\infty
    \end{aligned}
    $$

如果存在一组可行解$x_1, \ldots, x_k$满足$k\ra\infty$时$f_0(x_k)\ra -\infty$，称优化问题**无下界**。

如果存在$x^*\in X, f_0(x^*) = p^*$，则称$x^*$为**最优解**，全体最优解的集合为**最优集**。若最优集非空，称优化问题**可解**。当问题不可解时，集合$\{x | x\in X, f_0(x) \leq p^* + \varepsilon\}$称为优化问题的**$\varepsilon$-次优集**。

!!! theorem "最优值不可达的优化问题"

    设约束问题为$\eqref{2}$，以下问题都是最优值不可达的优化问题：

    $$
    \optim{\min}{f_0(x)}{x > 0}
    \label{2}
    $$

    * 当$f_0(x) = 1/x$时，$p^* = 0$，但最优集为空。
    * 当$f_0(x) = -\log x$时，$p^* = -\infty$，优化问题无下界。

如果$x_0$满足$\eqref{3}$，称为**局部最优**。

$$
\begin{gathered}
    & x_0\in X \\
    & \forall z\in X, \Vert z - x_0\Vert_2\leq R, f_0(z)\geq f_0(x_0)
\end{gathered}
\label{3}
$$

若$f_i(x^*) = 0$，称不等式约束$f_i$在最优值处**起作用**，否则**不起作用**。如果从优化问题中删除某个约束不会影响可行域，称约束**冗余**。

!!! theorem "可行性问题"

    当目标函数$f_0(x) = 0$时，优化问题是一个可行性问题，此时有

    $$
    \begin{gathered}
    p^* = -\infty \Lolra X = \varnothing \\
    p^* = 0 \Lolra X \not = \varnothing
    \end{gathered}
    $$

标准形式的优化问题满足如下条件：

* 约束的右端项为零
* 优化目标为极小化目标函数
* 除了非负约束以外，不包含$\geq$约束

### 问题的等价变换

一些优化问题的性质可能不够强导致难以进行优化，此时可以通过一些等价变换，将原本的优化问题转变为性质较强的凸优化问题。

#### 变量代换

设函数$\phi: \bbR^n\ra\bbR^n$是双射，且函数的值域包含问题的定义域，则如下优化问题与原问题$\eqref{1}$等价：

$$
\optim{\min}{f_0(\phi(z))}{\cases{
    \begin{aligned}
        & f_i(\phi(z))\leq 0 & i = \oneto m \\
        & h_i(\phi(z)) = 0 & i = \oneto p
    \end{aligned}
}}
$$

#### 函数代换

设函数$\psi_0: \bbR\ra\bbR$单调递增，$\psi_{1}, \ldots, \psi_{m}$满足$u\leq 0\Lora \psi_{i}(u) = 0$，$\phi_{1}, \ldots, \psi_{p}$满足$u = 0\Lora \phi_i(u) = 0$，则如下优化问题与原问题$\eqref{1}$等价：

$$
\optim{\min}{\psi_0(f_0(x))}{\cases{
    \begin{aligned}
        & \psi_i(f_i(z))\leq 0 & i = \oneto m \\
        & \phi_i(h_i(z)) = 0 & i = \oneto p
    \end{aligned}
}}
$$

#### 消除不等式约束

可以通过加入非负变量的方式将不等式约束转化为等式约束和非负约束。

$$
\optim{\min}{f_0(x)}{\cases{
    \begin{aligned}
        & s_i\geq 0 & i = \oneto m \\
        & f_i(x) + s_i 0 & i = \oneto m \\
        & h_i(x) = 0 & i = \oneto p
    \end{aligned}
}}
$$

称$s_i$为**松弛变量**，此时的优化问题共有$n + m$个优化变量。

#### 消除等式约束

设等式约束的解集可以用双射$\phi: \bbR^k\ra\bbR^n$表示，则原问题$\eqref{1}$与如下问题等价：

$$
\optim{\min}{f_0(\phi(z))}{f_i(\phi(z))\leq 0}
$$

对于线性等式约束$Ax - b = 0$，存在一个线性函数$\phi(z) = Fz + x_0$，其中$x_0$为$Ax - b = 0$的一个特解，$F$为矩阵$A$的零空间的一组基构成的矩阵。

#### 优化部分变量

注意到$\inf_{x}\inf{y} f(x, y) = \inf_{(x, y)}f(x, y) = \inf_{y}\inf_x f(x, y)$，因此可以先优化一部分变量，再优化另一部分变量，由此得到的优化问题与原问题$\eqref{1}$等价。

#### 上境图问题

如下问题与原问题$\eqref{1}$等价：

$$
\optim{\min}{t}{\cases{
    \begin{aligned}
        & f_0(x) - t\leq 0 \\
        & f_i(x)\leq 0 & i = \oneto m \\
        & h_i(x) = 0 & i= \oneto p
    \end{aligned}
}}
$$

## 凸优化问题及其性质

$\eqref{4}$是标准形式的**凸优化问题**：

$$
\optim{\min}{f_0(x)}{\cases{
    \begin{aligned}
        & f_i(x)\leq 0 & i = \oneto m \\
        & A^\top x = b
    \end{aligned}
}}
\label{4}
$$

并且，有

* $A\in \bbR^{p\times n}, b\in \bbR^p$
* $f_i, i\in 0, \ldots, m$是凸函数。

如果$f_0(x)$是拟凸函数，则为**拟凸优化问题**。

### 凸优化问题的性质

凸优化问题满足如下性质

* 可行域是凸集
* 任意局部最优解都是全局最优解
* 如果$f_0$可微，则$\forall x\in X, \nabla f_0(x)^\top (x - x^*)\geq 0$
    * 对于无约束优化问题，方程$\nabla f_0(x) = 0$的解即为最优
    * 对于仅包含线性等式约束$Ax - b = 0$的问题，方程$\nabla f_0(x)^\top v = 0, v\in \ker A$的解为最优
    * 对于仅包含符号约束$x\succeq 0$的问题，$\nabla f_0(x)\succeq 0, \nabla f_0(x)^\top x = 0$的解即为最优（解和此处的梯度至少有一个分量为零）。

### 保凸运算

对凸优化问题进行如下变换，得到的问题仍然是凸优化问题

* 消除等式约束
* 引入（线性）等式约束
* 引入松弛变量
* 转化为上境图问题
* 分步优化变量

### 拟凸优化问题的性质

拟凸优化问题存在（不是全局最优的）局部最优解。对于可微的拟凸函数$f_0$，如下性质仍然成立：

$$
\forall x\in X, \nabla f_0(x)^\top (x - x^*)\geq 0
$$

但使得$\forall x\in X, \nabla f_0(x)^\top (x - y)\geq 0$成立的$y$不一定是全局最优解。拟凸优化问题最优解的充要条件为

$$
\nabla f_0(x)^\top (y - x) > 0, y\in X - \{x\}
$$

拟凸函数的下水平集是凸集，因此可以使用一组凸函数组成的不等式条件表示其下水平集。由此，拟凸优化问题可以对目标函数值进行二分以构造相应的凸优化问题求解最优值$p^*$。对于形如$\eqref{4}$的拟凸优化问题，构造可行性问题$\eqref{5}$：

$$
\optim{\min}{0}{\cases{
    \begin{aligned}
        & \phi(x; t)\leq 0 \\
        & f_i(x)\leq 0 & i = \oneto m \\
        & Ax=b
    \end{aligned}
}}
\label{5}
$$

其中$\phi(x, t): \bbR^n\times \bbR\ra\bbR$是满足$f_0(x) \leq t\Lolra \phi(x, t)\leq 0$的凸函数。

如果对于某个$t$，优化问题$\eqref{5}$可行，则在$f_0(x) \geq t$的区间内寻找最优值，否则在$f_0(x) < t$的区间内寻找。

## 几何规划 - 转化为凸优化问题

形如$\eqref{5}$的函数称为**单项式**，单项式的和称为**正项式**。

$$
f(x) = c\prod_{i=1}^n x_i^{a_i}
\label{5}
$$

式中，$x\in \bbR^n_{\plus\plus}, c > 0$。

形如$\eqref{6}$的优化问题为**几何规划**（GP）

$$
\optim{\min}{f_0(x)}{\cases{
    \begin{aligned}
        & f_i(x)\leq 1 & i = \oneto m \\
        & h_i(x) = 1 & i = \oneto p
    \end{aligned}
}}
\label{6}
$$

其中$f_i$为正项式，$h_i$为单项式。

几何规划问题不是凸优化问题，但是可以转化为等价的凸优化问题。

## 一些常见的凸优化问题

### 线性规划问题

如果$\eqref{4}$中的目标函数和不等式约束都是线性函数时，此时的优化问题为**线性规划（LP）**。

$$
\optim{\min}{c^\top x + d}{\cases{
    \begin{aligned}
        & Gx\preceq h \\
        & Ax = b
    \end{aligned}
}}
$$

消除线性规划目标函数中的常数项、引入松弛变量以消除不等式约束、使用非负变量表示无约束变量，可以得到线性规划的标准形式：

$$
\optim{\min}{c^\top x}{\cases{
    \begin{aligned}
        & A^\top x = b \\
        & x\succeq 0
    \end{aligned}
}}
\label{7}
$$

如果$\eqref{4}$中的目标函数是线性函数之比，约束条件时线性函数，此时得到**线性分式规划**问题。

$$
\optim{\min}{\frac{c^\top x + d}{e^\top x + f}}{\cases{
    \begin{aligned}
        & Gx\preceq h \\
        & Ax = b
    \end{aligned}
}}
$$

线性分式规划问题是拟凸优化问题，可以转化如下的线性规划问题

$$
\optim{\min}{c^\top y + dz}{\cases{
    \begin{aligned}
        & Gy - hz\preceq 0 \\
        & Ay - bz = 0 \\
        & e^\top y + fz = 1 \\
        & z\geq 0
    \end{aligned}
}}
$$

由于一组拟凸函数的最大值仍是拟凸函数，可以将线性分式规划问题的目标函数替换为一组分式函数的最大值，此时的优化问题仍然是拟凸优化问题。

### 二次优化问题

如果$\eqref{4}$中的目标函数和不等式约束都是凸二次型，此时的优化问题为**二次约束二次规划**（QCQP）问题。

$$
\optim{\min}{\frac 12x^\top P_0x + q_0^\top x + r}{\cases{
    \begin{aligned}
        & \frac 12x^\top P_ix + q_i^\top x + r_i\leq 0 & i = \oneto m \\
        & Ax = b
    \end{aligned}
}}
\label{8}
$$

式中$P_i\in \bbS^n_\plus, q_i\in \bbR^n, A\in \bbR^{p\times n}$。

如果$\eqref{8}$中的不等式约束是线性的，则称为**二次规划问题**（QP）。

$$
\optim{\min}{\frac 12x^\top Px + q^\top x + r}{\cases{
    \begin{aligned}
        & Gx\preceq h \\
        & Ax = b
    \end{aligned}
}}
\label{9}
$$

式中$G\in \bbR^{m\times n}$

### 二阶锥规划

当$\eqref{4}$中的目标函数为线性函数，不等式约束构成二阶凸锥，此时的优化问题是**二阶锥规划**（SOCP）。

$$
\optim{\min}{f^\top x}{\cases{
    \begin{aligned}
        & \Vert A_ix + b\Vert_2\leq c_i^\top x + d_i & i = \oneto m \\
        & Fx = g
    \end{aligned}
}}
\label{10}
$$

称$\Vert A_ix + b\Vert_2\leq c_i^\top x + d_i$为**二阶锥约束**。

## 广义不等式下的凸优化问题

本节讨论$f_i: \bbR^n\ra\bbR^{k_i}$在$\preceq_{K_i}$情形下的优化问题。

### 广义不等式约束

形如下式的优化问题称为广义不等式约束的凸优化问题。

$$
\optim{\min}{f_0(x)}{\cases{
    \begin{aligned}
        & f_i\preceq_{K_i} 0 & i = \oneto m \\
        & Ax = b
    \end{aligned}
}}
$$

式中$f_0: \bbR^n\ra\bbR$，$K_i\subseteq \bbR^{k_i}$为正常锥，$f_i: \bbR^n\ra\bbR^{k_i}$为$K_i$-凸函数。大多数凸优化问题的结论在广义不等式下仍然成立。

#### 锥规划

锥规划是具有如下形式的凸优化问题

$$
\optim{\min}{c^\top x}{\cases{
    \begin{aligned}
        & Fx + g\preceq_K 0 \\
        & Ax = b
    \end{aligned}
}}
$$

当$K = \bbR^n_{\plus\plus}$时，锥规划退化为LP。仿照LP可以定义标准形式的锥规划问题。

$$
\optim{\min}{c^\top x}{\cases{
    \begin{aligned}
        & x\succeq_K 0 \\
        & Ax = b
    \end{aligned}
}}
$$

#### 半定规划

当$K\in \bbS^k_{\plus}$时，相应的锥规划为**半定规划**（SDP）。

$$
\optim{\min}{c^\top x}{\cases{
    \begin{aligned}
        & \sum_{i=1}^n x_iF_i + G\preceq 0 \\
        & Ax = b
    \end{aligned}
}}
$$

式中$G, F_i\in \bbS^k$。若这些矩阵都是对角矩阵，SDP退化为LP。不等式约束$\sum_{i=1}^n x_iF_i\preceq G$称为**线性矩阵不等式**（LMI），可以通过分块对角矩阵将多个LMI组合在一起。

标准形式的半定规划为

$$
\optim{\min}{\mathbf{tr}(CX)}{\cases{
    \begin{aligned}
        & \mathbf{tr(A_iX)} = b_i & i = \oneto p \\
        & X\succeq 0
    \end{aligned}
}}
$$

## 凸优化问题的包含关系

* 当QP目标函数中的$P = 0$时，QP退化为LP问题
* 当QCQP约束条件中的$P_i = 0$时，QCQP退化为QP问题
* 当SOCP约束条件中的$c_i = 0$时，SOCP退化为QCQP
* 形如$\eqref{10}$的SOCP与如下SDP问题等价

$$
\optim{\min}{f^\top x}{\cases{
    \begin{bmatrix}
        (c_i^\top x + d_i)I & A_ix + b_i \\
        (A_ix + b_i)I & (c_i^\top + d_i)
    \end{bmatrix}\succeq_{\bbS_\plus^n} 0
}}
$$

因此，有

$$
\text{LP}\subseteq \text{QP}\subseteq \text{QCQP}\subseteq \text{SOCP}\subseteq \text{SDP}
$$