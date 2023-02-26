# 凸优化

$\renewcommand{\geq}{\geqslant}\renewcommand{\leq}{\leqslant}\newcommand{\bs}{\boldsymbol}$

## Notations and Definitions

本节列举一些符号的表述，并借此回顾相关的数学概念

### 域
    * $\mathbb R, \mathbb N, \mathbb Z, \mathbb C$：实数域、自然数域、整数域、复数域
    * ${}_+, {}_{++}$分别表示非负、严格正

### 矩阵与向量

$A\in \mathbb R^{m\times n}$表示$A$是一个$m$行$n$列的实矩阵，其中的元素为$a_{ij}$，某列（或某行）的切片为$A_{\cdot j}$

$\boldsymbol x\in \mathbb R^m$表示$\boldsymbol x$是一个$m$维的实向量

方阵是行数与列数相等的矩阵，$A\in \mathbb R^{n\times n}$。对称矩阵满足$A^\top = A$，反对称矩阵满足$A^\top = - A$。对于复方阵$A\in \mathbb C^{n\times n}$，定义共轭转置（Hermitian）矩阵为$A^* = \overline {A^\top}$。

矩阵的迹是对角线上各个元素之和

$$
\mathrm {tr}(A) = \sum_{i=1}^n a_{ii}
$$

???+ theory "迹的性质"
    
    1. $\mathrm {tr}(A) = \mathrm {tr}(A^\top)$
    2. $\mathrm {tr}(A+B) = \mathrm {tr}(A) + \mathrm {tr}(B)$
    3. $\mathrm {tr}(t\cdot A) = t\cdot \mathrm {tr}(A)$
    4. $\mathrm {tr}(AB) = \mathrm {tr}(BA)$（不要求$A, B, \cdots$为方阵，只需要满足运算结果为方阵即可；对于多个元素，乘法顺序需要满足轮换对称性才能保证等式成立）

矩阵的范数是满足以下性质的函数$f$

1. 非负性：$f(\boldsymbol{x}) \geq 0$
2. 规范性：$f(\boldsymbol{x}) = 0 \Leftrightarrow \boldsymbol x = 0$
3. 齐次性：$f(t\cdot \boldsymbol{x}) = t\cdot f(\boldsymbol{x})$
4. 三角不等式：$f(\boldsymbol x + \boldsymbol y)\leq f(\boldsymbol x) + f(\boldsymbol y)$

???+ theory "常见的范数"

    1. 1-范数：$f(\boldsymbol{x}) = \sum_{i=1}^n \left|x_i\right|$
    2. 2-范数：$f(\boldsymbol{x}) = \sqrt{\sum_{i=1}^n \left|x_i^2\right|}$
    3. $\infty$-范数：$f(\boldsymbol{x}) = \sqrt[\infty]{\sum_{i=1}^n \left|x_i^\infty\right|}$
    4. 0-范数（不满足定义3，因此不是范数）：$f(\boldsymbol{x}) = \sum_{i=1}^n \boldsymbol{1}_{\{x_i \not = 0\}}$
    5. $l_p$-范数：$f(\boldsymbol{x}) = \sqrt[p]{\sum_{i=1}^n \left|x_i^p\right|}$
    6. Frobenius范数：$f(A) = \sqrt{\sum_i\sum_j a_{ij}^2} = \sqrt{\mathrm{tr}(A^\top A)}$

范数等价定理：对于两个范数$f, g$，存在正常数$c$使得$\forall \boldsymbol{x}, f(\boldsymbol{x}) \leq cg(\boldsymbol{x})$

设$f$为$\mathbb R^n$上的范数，对偶范数$f_*$定义如下

$$
f_*(\boldsymbol{x}) = \sup_{\boldsymbol{x}} \{\boldsymbol{z^\top x} | f(\boldsymbol{x}) \leq 1\}
$$

???+ theory "对偶范数"

    * 对偶范数的对偶范数不一定是原范数。
    * $p$-范数的对偶范数是$q$-范数，满足
        $$
        \frac{1}{p} + \frac{1}{q} = 1\qquad p, q\geq 1
        $$
        