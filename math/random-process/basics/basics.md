# 预备知识

## 可测空间、概率空间与概率测度

$\renewcommand{\geq}{\geqslant}\renewcommand{\leq}{\leqslant}$
当一个试验的结果无法预先确定时，称该实验为**随机试验**。随机试验可能出现的所有结果集合构成样本空间$\Omega$，每个可能的结果称为样本点$\omega$。$\Omega$的子集构成的集合称为**集类**$\mathcal F$。

!!! definition "可测空间"

    设$\mathcal F$为由$\Omega$的某些子集构成的非空集类，若满足以下条件：

    1. 若$A\in \mathcal F$，则$A^C = \Omega - A\in \mathcal F$。
    2. 若$A_n\in \mathcal F$，则$\bigcup\limits_{n=1}^\infty A_n \in \mathcal F$

    称$\mathcal F$为**$\sigma$域**，$(\Omega, \mathcal F)$为**可测空间**。

$\sigma$域$\mathcal F$对$\cap, \cup, -$运算封闭，任何元素经过可列次运算后仍属于$\mathcal F$。

对于集类$\mathcal A$，包含$\mathcal A$的$\sigma$域的交称为$\mathcal A$生成的$\sigma$域，记作$\sigma(\mathcal A)$。如：$\sigma(\{\varnothing, A, \Omega\}) = \{\varnothing, A, A^C, \Omega\}$。特殊地，记$\mathcal B = \sigma(\{(-\infty, \alpha], \forall \alpha \in \mathbb R\})$为Borel域。Borel域解决了样本空间在$\mathbb R$上连续的问题。可以证明，$\forall a < b, [a, b]\in \mathcal B, (a, b]\in \mathcal B, [a, b)\in \mathcal B, (a, b)\in \mathcal B$。定义$\mathcal B[a, b]$为限制在$[a, b]$上的Borel域。

!!! definition "概率测度与概率空间"

    设$(\Omega, \mathcal F)$为可测空间，$P: \mathcal F\rightarrow [0, 1]$为定义在$\mathcal F$上的集函数。且$P$满足

    1. 非负性：$\forall A\in \mathcal F, P(A)\geq 0$
    2. 规一性：$P(\Omega) = 1$
    3. 可列可加性：若$\forall i\in \mathbb N, A_i\in \mathcal F$，且$\forall i\not = j, A_i\cap A_j=\varnothing$，则

        $$
        P\left(\bigcup_{n=0}^\infty A_n\right) = \sum_{n=0}^\infty P(A_n)
        $$

    称$P$为可测空间$(\Omega, \mathcal F)$上的**概率测度**，$(\Omega, \mathcal F, P)$为**概率空间**。$\mathcal F$为**事件域**，$A\in \mathcal F$为**（随机）事件**

概率测度$P$满足如下性质

1. 有限可加性：可以令$A_{n+1} = A_{n+2} = \cdots = \varnothing$，结合可列可加性推出
2. $P(A^C) = 1 - P(A)$
    * $P(\varnothing) = 0$
3. 集合的包含关系：$A\subset B\Rightarrow P(A)\leq P(B)$
4. 容斥原理：

    $$
    P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{1\leq i < j\leq n}P(A_i\cap A_j) + \cdots + (-1)^{n+1}P(A_1\cap \cdots \cap A_n)
    $$

    * $P(A\cup B) = P(A) + P(B) - P(A\cap B)$
    * $P(A - B) = P(A\cup B) - P(B) = P(A) - P(A\cap B)$
    * $P\left(\bigcup_{i=1}^n A_i\right)\leq \sum_{i=1}^n P(A_i)$

满足$A_n\subset A_{n+1}$的事件列$\{A_n, n\geq 1\}$称为单调增序列，满足$A_n\supset A_{n+1}$的事件列$\{A_n, n\geq 1\}$称为单调减序列。由此可以定义事件列的极限：

1. 若$\{A_n, n\geq 1\}$为单调增序列，则$\lim\limits_{n\rightarrow \infty}A_n = \bigcup_{i=1}^\infty A_i$
2. 若$\{A_n, n\geq 1\}$为单调减序列，则$\lim\limits_{n\rightarrow \infty}A_n = \bigcap_{i=1}^\infty A_i$

事件列的极限满足

$$
\lim_{n\rightarrow\infty}P(A_n) = P\left(\lim_{n\rightarrow\infty} A_n\right)
$$

可以证明，单点集$\{a\}$为事件列$\{[a, a+1/n], n > 0\}$的极限。

!!! theorem "Borel-Cantelli引理"

    设$\{A_n, n\geq 1\}$为事件序列，满足$\sum_{i=1}^\infty P(A_i) < \infty$，则

    $$
    P\left(\lim_{i\rightarrow\infty}\sup A_i\right) \triangleq P\left(\bigcap_{n=1}^\infty \bigcup_{i=n}^\infty A_i\right) = 0
    $$

定义条件概率

$$
P(A|B) = \frac{P(A\cap B)}{P(B)}
$$

若事件$A, B$满足$P(A\cap B) = P(A)P(B)$，则称事件$A, B$相互独立，且$P(A|B) = P(A)$。同理可以推广至$n$个事件相互独立的情况。设$A_1, \cdots, A_n\in \mathcal F$，若对于其中任意$k$个事件，都有

$$
P(A_{i_1}\cap\cdots\cap A_{i_k}) = P(A_{i_1})\cdots P(A_{i_k})
$$

称$A_1, \cdots, A_n$相互独立。

若$\{A_n, n\geq 1\}$为相互独立的事件序列，且$\sum_{n=1}^\infty P(A_n) = \infty$，则

$$
P\left(\lim_{i\rightarrow\infty}\sup A_i\right) \triangleq P\left(\bigcap_{n=1}^\infty \bigcup_{i=n}^\infty A_i\right) = 1
$$

## 随机变量与分布函数

设样本空间为$\Omega$。

### 随机变量

设$(\Omega, \mathcal F, P)$为概率空间，$X(\omega)$为定义在$\Omega$上的单值实函数，即$X: \Omega\rightarrow \mathbb R$，若$\forall a\in \mathbb R$，有$\{\omega:  X(\omega) \leq a\}\in \mathcal F$，称$X(\omega)$为随机变量，简记为$X$。定义$F(x) = P(X\leq x) = P(X\in (-\infty, X])$为$X$的分布函数。

* 离散型随机变量：随机变量$X$的可能取值的全体是可列集或者有限集。
* 连续型随机变量：若$\forall B\in \mathcal F$，存在一个函数$f(x)$满足

    $$
    P(X\in B) = \int_B f(x)\mathrm dx
    $$

    称$X$为连续型随机变量，$f(x)$为$X$的概率密度函数。

!!! definition "概率密度函数与概率分布函数"

    根据概率分布函数的定义，有

    $$
    P(x < X\leq x + h) = F(x + h) - F(x) = \int_{x}^{x + h} f(x)\mathrm dx = f(x)h + o(h)
    $$

    令$h\rightarrow 0$并取极限，得到

    $$
    \frac{\mathrm dF(x)}{\mathrm dx} = \lim_{h\rightarrow 0} \frac{F(x + h) - F(x)}{h} = f(x)
    $$

对于二维随机变量$X, Y$，定义联合分布函数为$F(x, y) = P(X\leq x, Y\leq y)$，边缘分布为$F_X(x) = P(X\leq x), F_Y = P(Y\leq y)$。同理可以定义概率密度函数$f(x, y)$：

$$
F(x, y) = \int_{-\infty}^x\int_{-\infty}^y f(v, u)\mathrm du\mathrm dv
$$

若$F(x, y) = F_X(x)F_Y(y)$，称$X$与$Y$相互独立。

### 数字特征

设$X$为随机变量，分布函数为$F(x)$，若$\int_{-\infty}^\infty |x|\mathrm dF(x)$存在，则定义$X$的期望$E(X)$为

$$
E(X) = \int_{-\infty}^\infty x\mathrm dF(x)
$$

数学期望$E(X)$满足

* 可加性

    $$
    E\left(\sum_{i=1}^n c_iX_i\right) = \sum_{i=1}^n c_iE(X_i)
    $$

* 函数

    $$
    E(g(x)) = \int_{-\infty}^\infty g(x)\mathrm dF(x)
    $$

对于离散型随机变量，有

$$
E(X) = \sum_{i=1}^\infty x_nP(X = x_n)
$$

对于连续型随机变量，有

$$
E(X) = \int_{-\infty}^\infty xf(x)\mathrm dx
$$

若随机变量$X, Y$相互独立，则有

$$
\begin{aligned}
    E(XY) &= \int_{-\infty}^\infty \int_{-\infty}^\infty xyf(x, y)\mathrm dx\mathrm dy \\
    &= \int_{-\infty}^\infty \int_{-\infty}^\infty xyf_X(x)f_Y(y)\mathrm dx\mathrm dy \\
    &= \int_{-\infty}^\infty xf_X(x)\mathrm dx\int_{-\infty}^\infty yf_Y(y)\mathrm dy \\
    &= E(X)E(Y)
\end{aligned}
$$

定义随机变量$X$的方差为$\sigma_X^2 = D(X) = E(X - E(X)) = E(X^2) - E^2(X)$，定义随机变量$X, Y$的协方差为$\mathrm{cov}(X, Y) = E(XY) - E(X)E(Y)$，相关系数为$\rho = \mathrm{cov}(X, Y) / (\sigma_X\sigma_Y)$，$k$阶矩为$E(X^k)$

定义随机变量$X$的矩母函数为$\psi(t) = E\left(e^{tX}\right)$，特征函数为$\phi(t) = E\left(e^{\mathbf itX}\right)$

矩母函数满足如下性质

1. $E\left(X^k\right) = \psi^{(k)}(0)$
2. 设随机变量$X, Y$的分布函数为$F_X(t), F_Y(t)$，矩母函数为$\psi_X(t), \psi_Y(t)$，则$\psi_X(t) = \psi_Y(t) \Leftrightarrow F_X(t) = F_Y(t)$

特征函数满足如下性质

1. 设随机变量$X, Y$的分布函数为$F_X(t), F_Y(t)$，特征函数为$\phi_X(t), \phi_Y(t)$，则$\phi_X(t) = \phi_Y(t) \Leftrightarrow F_X(t) = F_Y(t)$
2. $i^kE(X^k) = \phi^{(k)}(0)$
3. 若$X, Y$相互独立，有$\phi_{X+Y}(t) = \phi_{X}(t) + \phi_{Y}(t)$

### 常见随机变量的分布

1. 二项分布：$X\sim B(n, p)$

    $$
    P(X = k) = \binom{n}{k} p^k(1 - p)^{n - k}
    $$

2. 泊松分布：$X\sim P(\lambda)$

    $$
    P(X = k) = \frac{\lambda^k}{k!}e^{-\lambda}
    $$

3. 几何分布：$X\sim G(p)$

    $$
    P(X = k) = (1 - p)^{k - 1}p
    $$

4. 均匀分布：$X\sim U(a, b)$

    $$
    f(x) = \left\{\begin{aligned}
        & \frac{1}{b-a} & a < x < b \\
        & 0 & \text{otherwise}
    \end{aligned}\right.
    $$

5. 正态分布：$X\sim N(\mu, \sigma^2)$

    $$
    f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
    $$

6. 指数分布：$X\sim E(\lambda)$

    $$
    f(x) = \left\{\begin{aligned}
        & \lambda e^{-\lambda x} & x\geq 0 \\
        & 0 & x < 0
    \end{aligned}\right.
    $$

### 条件数学期望

对于连续随机变量，条件数学期望$E(X|Y = y)$的定义如下：

$$
E(X|Y = y) = \int_{-\infty}^\infty x\frac{f(x, y)}{f_Y(y)}\mathrm dx
$$

定义$E(X|Y)$为$X$关于$Y$的条件数学期望

$$
E(X|Y) = \sum_j \boldsymbol 1_{\{Y = y_j\}}(\omega)E(X|Y=y_j)
$$

对于离散随机变量，条件数学期望$E(X|Y = y)$的定义如下：

$$
E(X|Y = y) = \sum_i x_iP(X=x_i | Y=y)
$$

显然，$E(X|Y = y)$是$y$的函数，定义随机变量$E(X|Y)$为$X$关于$Y$的条件期望，若$E(X|Y)$满足

1. $E(X|Y)$是$Y$的函数，当$Y = y$时，$E(X|Y) = E(X|Y = y)$
2. $\forall D\in \mathcal B$，有

    $$
    E[E(X|Y)|Y\in D] = E(X|Y\in D)
    $$

!!! theorem "条件数学期望的性质"

    条件数学期望满足如下性质：

    1. $E(E(X|Y)) = EX$
    2. 若$X, Y$相互独立，则$E(X|Y) = EX$
    3. $E[g(X)h(Y)|Y] = h(Y)E(g(X)|Y)\quad \text{a.s.}$

## 随机过程

随机过程是一族无穷多个，相互有关的随机变量。设$X(t, \omega)$为随机变量，其中$t\in T\subset \mathbb R$为参数。称$X_T = \{X(t, \omega), t\in T\}$为随机过程。

1. $X(t, \omega)$可以简记为$X(t)$；
2. 当$T$为可列集时，称$X_T$为随机序列；
3. $X_T$的取值范围称为状态空间$S$；
4. $X(\cdot, \omega), \omega\in \Omega$是关于$t$的函数，称为轨道。
