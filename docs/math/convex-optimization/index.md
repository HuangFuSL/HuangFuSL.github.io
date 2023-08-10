# 凸优化

## 目录

* [凸集](convex-set.md)
* [凸函数](convex-function.md)

## Notations and Definitions

本节列举凸优化中所用符号的表述，并借此回顾相关的数学概念

### 数域

* $\mathbb R, \mathbb N, \mathbb Z, \mathbb C$：实数域、自然数域、整数域、复数域
* 下标 ${}_\plus, {}_{\plus\plus}$ 在实数域和实向量域上分别表示非负、严格正，在实矩阵域上表示半正定、正定。

### 矩阵与向量

$A\in \mathbb R^{m\times n}$表示$A$是一个$m$行$n$列的实矩阵，其中的元素为$a_{ij}$，某列（或某行）的切片为$A_{\cdot j}$

$\boldsymbol x\in \mathbb R^m$表示$\boldsymbol x$是一个$m$维的实向量，$\boldsymbol 1$表示所有分量均为$1$的向量。

方阵是行数与列数相等的矩阵，$A\in \mathbb R^{n\times n}$。对称矩阵满足$A^\top = A$，反对称矩阵满足$A^\top = - A$。正定矩阵满足$\forall x\in \mathbb R^n, x^\top Ax > 0$，记作$A\succ 0$；半正定矩阵满足$\forall x\in \mathbb R^n, x^\top Ax \geq 0$，记作$A\succeq 0$。对于复方阵$A\in \mathbb C^{n\times n}$，定义共轭转置（Hermitian）矩阵为$A^* = \overline {A^\top}$。全体$k$阶对称矩阵的集合为$\mathbb S^k$。

矩阵的迹是对角线上各个元素之和

$$
\mathrm {tr}(A) = \sum_{i=1}^n a_{ii}
$$

???+ theorem "迹的性质"

    1. $\mathrm {tr}(A) = \mathrm {tr}(A^\top)$
    2. $\mathrm {tr}(A+B) = \mathrm {tr}(A) + \mathrm {tr}(B)$
    3. $\mathrm {tr}(t\cdot A) = t\cdot \mathrm {tr}(A)$
    4. $\mathrm {tr}(AB) = \mathrm {tr}(BA)$（不要求$A, B, \cdots$为方阵，只需要满足运算结果为方阵即可；对于多个元素，乘法顺序需要满足轮换对称性才能保证等式成立）

定义两个矩阵$X, Y$的内积为其乘积的迹$\mathrm{tr}(XY)$

## 范数

范数是满足以下性质的函数$f$

1. 非负性：$f(\boldsymbol{x}) \geq 0$
2. 规范性：$f(\boldsymbol{x}) = 0 \Leftrightarrow \boldsymbol x = 0$
3. 齐次性：$f(t\cdot \boldsymbol{x}) = t\cdot f(\boldsymbol{x})$
4. 三角不等式：$f(\boldsymbol x + \boldsymbol y)\leq f(\boldsymbol x) + f(\boldsymbol y)$

???+ theorem "常见的范数"

    1. 1-范数：$f(\boldsymbol{x}) = \sum_{i=1}^n \left|x_i\right|$
    2. 2-范数：$f(\boldsymbol{x}) = \sqrt{\sum_{i=1}^n \left|x_i^2\right|}$
    3. $\infty$-范数：$f(\boldsymbol{x}) = \sqrt[\infty]{\sum_{i=1}^n \left|x_i^\infty\right|}$
    4. 0-范数（不满足定义3，因此不是范数）：$f(\boldsymbol{x}) = \sum_{i=1}^n \boldsymbol{1}_{\{x_i \not = 0\}}$
    5. $l_p$-范数：$f(\boldsymbol{x}) = \sqrt[p]{\sum_{i=1}^n \left|x_i^p\right|}$
    6. Frobenius范数：$f(A) = \sqrt{\sum_i\sum_j a_{ij}^2} = \sqrt{\mathrm{tr}(A^\top A)}$

范数等价定理：对于两个范数$f, g$，存在正常数$c$使得$\forall \boldsymbol{x}, f(\boldsymbol{x}) \leq cg(\boldsymbol{x})$

设$f$为$\mathbb R^n$上的范数，对偶范数$f_*$定义如下

$$
f_*(\boldsymbol{z}) = \sup_{\boldsymbol{x}} \{\boldsymbol{z^\top x} | f(\boldsymbol{x}) \leq 1\}
$$

???+ theorem "对偶范数"

    * 对偶范数的对偶范数不一定是原范数。
    * $p$-范数的对偶范数是$q$-范数，满足

        $$
        \frac{1}{p} + \frac{1}{q} = 1\qquad p, q\geq 1
        $$

根据范数可以定义球的概念

???+ definition "球"

    给定$\mathbb R^n$空间中的范数$\Vert\cdot\Vert$，$B(x, r)$表示范数$\Vert \cdot\Vert$中的（开）球，即

    $$
    B(x, r) = \{y | \Vert y - x\Vert < r\}
    $$

    $\bar B(x, r)$表示一个闭球

    $$
    \bar B(x, r) = \{y | \Vert y - x\Vert \leq r\}
    $$

### 集合

设集合$C\subseteq \mathbb R^n, x\in C$，使用2-范数度量距离。

* 若$\exists r \in \mathbb R_{\plus\plus}, B(x, r)\subseteq C$，称$x$为**内点**。全体内点构成集合的**内部**$C^\circ$，显然$C^\circ \subseteq C$。
* 若$\forall r\in \mathbb R_{+}, B(x, r)\cap C \not = \varnothing, B(x, r) \cap C^C \not = \varnothing$，称$x$为**边界点**。全体边界点构成集合的**边界**$\partial C$。
    * 根据边界点的定义，有$\partial C = \partial C^C$。
* 若$x$不是内点，则$x$为边界点，即$\partial C \cup C^\circ = C, \partial C\cap C^\circ = \varnothing$。

若集合$C$中的所有点都是内点，即$C^\circ = C$，称$C$为**开集**。若$C$不是开集，则$C$为**闭集**。开集的补集是闭集。

定义闭包为

$$
\mathbf{cl}C = \{x \in \mathbb R^n| \forall r\in \mathbb R_{++}, B(x, r)\cap C\not = \varnothing\}
$$

直观上，闭包可以理解为$C\cup \partial C^C$，即集合与其补集的边界的并。

$\varnothing, \mathbb R^n$既是开集也是闭集：

* $\varnothing$的闭包仍为$\varnothing$，所以是闭集；然而$\varnothing^\circ = \varnothing$，所以是开集。
* $\varnothing^C = \mathbb R^n$，所以$\mathbb R^n$既是开集也是闭集。
