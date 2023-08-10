# 凸函数及其性质

凸函数是一类函数上方（上境图，epigraph）是凸集的函数，即函数曲线上任意两点连成的线段都在函数曲线的上方。

若函数$f: \mathbb R^n\rightarrow \mathbb R$满足**琴生不等式**：

$$
f(\theta x + (1 - \theta)y)\leq \theta f(x) + (1 - \theta)f(y), 0\leq \theta\leq 1
$$

，则称$f$为**凸函数**。

???+ theorem "琴生不等式的扩展"

    琴生不等式可以扩展到更多点的凸组合上，对于凸函数$f$，设$\theta_1, \ldots, \theta_k\geq 0, \theta_1 + \cdots + \theta_k = 1$，则

    $$
    f(\theta_1 x_1 + \cdots + \theta_k x_k)\leq \theta_1 f(x_1) + \cdots + \theta_k f(x_k)
    $$

    该式可以进一步拓展至级数、积分、期望等形式。

若$f(\theta x + (1 - \theta)y)< \theta f(x) + (1 - \theta)f(y), 0\leq \theta\leq 1$，则为**严格凸函数**。凸函数的上境图（$\mathbf{epi}f$）是凸集。

如果$-f$是凸函数，则$f$为**凹函数**，若$-f$是严格凸函数，则$f$为**严格凹函数**。凹函数的亚图（$\mathbf{hypo}f$）是凸集。

所有的线性函数都既是凸函数也是凹函数。

$f$是凸函数当且仅当$f$在定义域内任何直线上都是凸函数，即

$$
\forall v,\forall x, g(t; v, x) = f(x + tv)
$$

是凸函数。

记$f$的延伸$\tilde f$为分段函数

$$
\tilde f(x) = \left\{\begin{aligned}
    & f(x) & x\in \mathbf{dom}f \\
    & \infty & x\not\in \mathbf{dom}f
\end{aligned}\right.
$$

类似地，对于凹函数可以将其定义域外的部分延伸至$-\infty$。 在优化问题中，可以使用示性函数$\tilde I_C(x) = 0, x\in C$来将优化问题的解限定到凸集$C$上。$\tilde I_C(x)$是凸函数。

其他的凸函数还有

* 指数函数$f: \mathbb R\rightarrow\mathbb R = e^{ax}, a\in \mathbb R$
* 幂函数$f: \mathbb R_{ + + }\rightarrow\mathbb R = x^a, a\geq 1$或$a\leq 0$
* 绝对值幂函数$f: \mathbb R\rightarrow\mathbb R = |x|^p, p\geq 1$
* 负对数函数$f: \mathbb R_{\plus\plus}\rightarrow \mathbb R = -\log x$
* 负熵$f: \mathbb R_{\plus\plus}\rightarrow \mathbb R = x\log x$
* 范数（三角不等式）
    * 最大值函数相当于无穷阶范数$\Vert\cdot\Vert_\infty$，因此也是凸的。
* 指数和的对数$f: \mathbb R^n\rightarrow \mathbb R = \log \sum_{i=1}^n e^{x_i}$

对于任意$\alpha$，凸函数的下水平集$\{x\in \mathbf{dom} f | f(x) \leq \alpha\}$是凸集。或者说，凸函数的等高线是凸集。

## 一阶条件与二阶条件

### 一阶条件

若$f$的***定义域为凸集***且可微，则$f$是凸函数等价于

$$
f(y) \geq f(x) + (\nabla f(x))^\top (y - x)
$$

凸函数的一阶近似是凸函数值的全局下估计。

{{ latex_image('imgs/first-order-convex.tex', 'first-order-convex') }}

一阶条件同样也能用来反映严格凸函数、凹函数和严格凹函数。

### 二阶条件

若$f$的***定义域为凸集***且二阶可微，则$f$是凸函数等价于

$$
\nabla ^2f(x)\succeq 0
$$

二阶条件也可以用来反映严格凸函数、凹函数和严格凹函数。注意严格凸函数不一定满足$\nabla^2 f(x)\succ 0$，严格凹函数同理。

## 保凸运算

对于函数$f, g, f_1, \ldots f_k: \bbR^n\rightarrow \bbR$（如未指明，则假定为凸函数），以下函数仍为凸函数：

* 凸函数的线性组合：$f'(x) = \sum_{i=1}^k \theta_i f_i(x)$

    ???+ theorem "扩展到积分形式"

        设$f(x, y)$对于任意$y$，关于$x$都为凸函数，函数$w(y)$满足$w(y)\geq 0$，则

        $$
        g(x) = \int_{\mathcal A} w(y)f(x, y)\dd y
        $$

        为凸函数。

* 仿射变换：$f'(x): \bbR^m\rightarrow \bbR = f(Ax + b)$，其中$A\in \bbR^{m\times n}, b\in \bbR^n$
* 逐点最大：$f'(x) = \max\{f_1(x), \ldots, f_k(x)\}$

    逐点最大可以理解为一系列函数上境图的交集，对于$f'$，有

    $$
    \mathbf{epi} f' = \bigcap_{i=1}^k \mathbf{epi} f_k
    $$

    根据凸集的保凸性质可知，$\mathbf{epi} f'$是凸集。

    ???+ theorem "扩展到无限个函数的形式"

        设$f(x, y)$对于任意$y$，关于$x$都为凸函数，则

        $$
        g(x) = \sup_{y\in \calA} f(x, y)
        $$

        也为凸函数。

* 复合函数：$g\circ f$
    * 当$g: \bbR\rightarrow \bbR$时，$f' = g\circ f = g(f(x))$满足
        1. 若$g$是凸函数且非减，$f$为凸函数，则$f'$为凸函数
        2. 若$g$是凸函数且非增，$f$为凹函数，则$f'$为凸函数
    * 当$g: \bbR^k\rightarrow \bbR$时，$f' = g\circ f = g(f_1(x), \ldots, f_k(x))$是凸函数。
        1. 若$g$为凸函数，且在各个分量上非减，$f_i$为凸函数，则$f'$为凸函数
        2. 若$g$是凸函数，且在各个分量上非增，$f_i$为凹函数，则$f'$为凸函数

* 最小化：若$f(x, y): \bbR^m\times \bbR^n\rightarrow \bbR$是凸函数，则对于非空凸集$C$，$\inf_{y\in C}f(x, y)$为凸函数。
* 透视函数：$g(x, t) = tf(x / t)$是凸函数。

## 共轭函数

函数$f: \bbR^n\rightarrow \bbR$的共轭函数$f^*: \bbR^n\rightarrow\bbR$为

$$
f^*(y)\triangleq \sup_{x\in \mathbf{dom}f} (y^\top x - f(x))
$$

共轭函数是凸函数。$f^{**}$不一定和$f$相等，当且仅当$f$为凸函数时，$f^{**} = f$。

???+ proof "共轭函数的凸性"

    对于任意函数$f: \bbR^n\rightarrow \bbR$和$x\in \bbR^n$，$g(y, x) = y^\top x - f(x)$为线性函数（也是凸函数）

    $f^*(y)$为$g(y, x)$关于$x$的逐点上确界，因此为凸函数。

根据定义，函数$f$及其共轭满足

$$
f(x) + f^*(y)\geq x^\top y
$$

???+ theorem "二次函数的共轭"

    对于二次函数$f(x) = \frac{1}{2} x^\top Qx, Q\in \bbS_{\plus\plus}^n$，其共轭函数为

    $$
    f^*(y) = \frac{1}{2} y^\top Q^{-1}y
    $$

???+ theorem "范数的共轭"

    对于任意范数$\Vert\cdot\Vert$，其对偶范数为$\Vert\cdot\Vert_*$，则$f(x) = \Vert x\Vert$的共轭函数为

    $$
    f^*(y) = \left\{
    \begin{aligned}
        & 0 & \Vert y\Vert_* \leq 1 \\
        & \infty & \text{otherwise}
    \end{aligned}
    \right.
    $$

函数和的共轭等于其共轭的和

$$
(f + g)^* = f^* + g^*
$$

对于可微函数$f$，有

$$
\begin{gather*}
    f(y) = z^\top \nabla f(z) - f(z) \\
    \nabla f(z) = y
\end{gather*}
$$

???+ theorem "线性变换的共轭"

    设$g(x) = f(Ax + b)$，其中$A\in \bbR^{n\times n}$且满秩，则

    $$
    \begin{aligned}
    g^*(y) &= \sup_{x} (x^\top y - f(Ax + b)) \\
    &= \sup_{x} [A^{-1}[(Ax + b) - b]]^\top y - f(Ax + b) \\
    &= \sup_x [(A^{-1}(Ax + b))^\top y - f(Ax + b)] - b^\top A^{-\top}y \\
    &= \sup_x [(Ax+b)^\top (A^{-\top}y) - f(Ax + b)] - b^\top A^{-\top}y \\
    &= f^*(A^{-\top}y) - b^\top A^{-\top}y
    \end{aligned}
    $$

    设$h(x) = af(x) + b$，则：

    $$
    \begin{aligned}
    h^*(y) &= \sup_x y^\top x - af(x) - b \\
    &= \sup_{x} a(a^{-1}y^\top x - f(x)) - b \\
    &= af^*(a^{-1}y) - b
    \end{aligned}
    $$

## 拟凸函数

若函数$f$的下水平集$\{x|f(x)\leq \alpha\}$对于任意$\alpha$都为凸集，则$f$为**拟凸函数**。若$-f$为拟凸函数，则$f$为**拟凹函数**。若$f$既是拟凸函数，又是拟凹函数，则$f$为**拟线性函数**。

所有的凸函数都是拟凸函数。但拟凸函数不一定是凸函数，$\nabla f(x_0) = 0\not \Rightarrow f(x)\geq f(x_0)$

### 性质

拟凸函数满足如下性质

* 函数$f$是拟凸函数当且仅当$\mathbf{dom} f$是凸集，且$f$满足

    $$
    f(\theta x + (1 - \theta)y)\leq \max\{f(x), f(y)\}
    $$

* 对于定义在$\bbR$上的函数，$f$是拟凸函数当且仅当$f$满足如下条件其中之一
    * $f$是单调函数
    * $\exists x_0$，对于$x\geq x_0, f$非减，$x\leq x_0, f$非增
* 对于$\bbR\rightarrow \bbR$上的任意单调函数$f$，$-f$也是单调函数，因此$f$是拟线性函数。

### 一阶条件与二阶条件

（一阶条件）对于定义在凸集上的可微函数$f: \bbR^n\rightarrow \bbR, f$是拟凸函数当且仅当$f$满足

$$
\forall x, y\in \mathbf{dom}f, f(y) \leq f(x)\Longrightarrow \nabla f(x)^\top (y - x)\leq 0
$$

???+ theorem "一阶条件的几何解释"

    根据拟凸函数的定义，若对于任意$x$，其下水平集$S_x = \{y | f(y)\leq f(x)\}$均为凸集。

    根据凸集的性质，任何凸集都能表示成支撑超平面对应半空间的交集。集合$\{y | \nabla f(x)^\top (y - x)\leq 0\}$是下水平集$S_x$在$x$处支撑超平面对应的半空间。

（二阶条件）对于定义在凸集上的二次可微函数$f: \bbR^n\rightarrow \bbR, f$是拟凸函数当且仅当$f$满足

$$
\forall x\in \mathbf{dom} f, \nabla f(x) = 0\Longrightarrow \nabla^2 f(x)\succeq 0
$$

即$f$在梯度为$0$的地方，二阶梯度正定（非负）。

拟凸函数的二阶梯度最多只有一个负特征值。

### 保拟凸运算

设$f, g, f_1,\ldots, f_k$为拟凸函数。如未指明，这些函数定义在$\bbR^n \rightarrow \bbR$上。以下函数为拟凸函数：

* 非负加权最大值：设$w_1, \ldots, w_k\geq 0, f' = \max\{w_1f_1(x), \ldots, w_kf_k(x)\}$为拟凸函数。
* 复合函数：$f' = g\circ f$是拟凸函数，其中$g: \bbR\rightarrow \bbR$单调非减。
* 最小值：$f(x, y): \bbR^m\times \bbR^n\rightarrow \bbR$关于$x, y$是拟凸函数，则对于任意凸集$C, g(x) = \inf_{y\in C}f(x, y)$是拟凸函数。

## 对数-凸函数

定义$\log 0 = -\infty$。若对于函数$f: \bbR^n\rightarrow \bbR_{\plus}$，有$\log f$为凸函数，则称$f$为**对数-凸函数**。若$1 / f$为对数-凸函数，则$f$为**对数-凹函数**。

对数-凸函数是凸函数（指数函数$e^x$是凸函数），非负的凹函数是对数-凹函数，对数-凹函数是拟凹函数。

???+ theorem "对数-凹函数的充要条件"

    $f: \bbR^n \rightarrow \bbR$是对数-凹函数当且仅当

    $$
    f(\theta x + (1 - \theta)y)\geq f^\theta(x)f^{1 - \theta}(y)
    $$

    对于任意$x, y\in \mathbf{dom} f, 0\leq\theta\leq 1$成立。

    对于二次可微的对数-凹函数$f$，有

    $$
    f(x)\nabla^2 f(x)\preceq \nabla f(x)^\top \nabla f(x)
    $$

    对于任意$x\in \mathbf{dom} f$成立，反之亦然。

对数-凸函数之和仍是对数-凸函数（对数-凹函数之和不一定是对数-凹函数），对数-凸（凹）函数的乘积是对数-凸（凹）函数。

???+ theorem "对数-凸函数之和性质的拓展"

    设$f(x, y): \bbR^n\times \bbR^m\rightarrow \bbR$满足对于任意$y$，$f(x, y)$关于$x$是对数-凸函数，则

    $$
    \int_{y} f(x, y)\dd y
    $$

    是凸函数。

## 广义不等式定义的凸性

设$K$为正常锥，定义$f(x)$的增减性如下。

* $f$为**$K$-增**，当且仅当$f$满足$x\succeq_K y, x\not = y\Longrightarrow f(x)\succ_K f(y)$，若$-f$为$K$-增函数，则$f$为$K$-非增函数。
* $f$为**$K$-非减**，当且仅当$f$满足$x\succeq_K y\Longrightarrow f(x)\succeq_K f(y)$

$f$是$K$-非减当且仅当$\nabla f\succeq_{K^*} 0$，$f$是$K$-增当且仅当$\nabla f\succ_{K^*} 0$。

$f$是**$K$-凸函数**当且仅当$\forall x, y, \theta f(x) + (1 - \theta) f(y)\succeq_K f(\theta x + (1 - \theta) y)$

$f$是**严格$K$-凸函数**当且仅当$\forall x\not = y, \theta f(x) + (1 - \theta) f(y)\succ_K f(\theta x + (1 - \theta) y)$

$f$是$K$-凸函数当且仅当$\forall w\succeq_{K^*} 0, w^\top f(x)$为凸函数；$f$是严格$K$-凸函数当且仅当$\forall w\succeq_{K^*} 0, w\not = 0, w^\top f$是严格凸函数。
