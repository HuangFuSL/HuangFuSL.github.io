# 1 行列式

## 1.1 行列式的定义

考虑如下形式的方程组：

$$
\left\{\begin{aligned}
    a_1x + b_1y &= d_1 \\
    a_2x + b_2y &= d_2
\end{aligned}\right.
$$

解得：

$$
\begin{aligned}
    (a_1b_2-b_1a_2)x &= d_1b_2-b_1d_2 \\
    (a_1b_2-b_1a_2)y &= a_1d_2-d_1a_2
\end{aligned}
$$

当$a_1b_2-b_1a_2\not = 0$时，此时有方程组有唯一解$\left\{\begin{aligned}x&=\frac{d_1b_2-b_1d_2}{a_1b_2-b_1a_2}\\ y&=\frac{a_1d_2-d_1a_2}{a_1b_2-b_1a_2}\end{aligned}\right.$

令：

$$
\begin{aligned}
    D &= \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1b_2-b_1a_2 \\
    D_1 &= \begin{vmatrix} d_1 & b_1 \\ d_2 & b_2 \end{vmatrix} = d_1b_2-b_1d_2 \\
    D_2 &= \begin{vmatrix} a_1 & d_1 \\ a_2 & d_2 \end{vmatrix} = a_1d_2-d_1a_2
\end{aligned}
$$

则方程的解可以记为$\left\{\begin{aligned}x &= \frac{D_1}{D} \\ y &= \frac{D_2}{D}\end{aligned}\right.$

同样地，从三阶方程组可以引入三阶行列式：

$$
\begin{aligned}
\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix} = &a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} \\ &- a_{31}a_{22}a_{13} - a_{21}a_{12}a_{33} - a_{32}a_{23}a_{11}
\end{aligned}
$$

从三阶行列式转换为$n$阶行列式，需要引入排列的概念。

> **定义** $n$阶排列是由整数$1, 2, \dots, n$组成的有序数组。

定义排列中的逆序对与逆序数：

> **定义** 对于一个$n$阶排列$a_1, \dots, a_n$，逆序对$a_i, a_j:=a_j<a_i, i<j$。  
> **定义** 对于一个$n$阶排列$a_1, \dots, a_n$，定义该排列的逆序数等于排列中逆序对的个数。称逆序数为奇数的排列为奇排列，逆序数为偶数的排列为偶排列，逆序数为0的排列为自然排列。

对于排列，有如下结论：

> **定理1.1** 对换排列中的任意两个元素，排列的奇偶性改变；  
> **定理1.2** 奇排列的个数与偶排列的个数相等；  
> **定理1.3** 可以通过有限次对换操作将任何排列转变为自然排列  

根据逆序数的定义、定理1.1与定理1.3，可以推出如下结论：

> **定理1.4** 将任意排列转变为自然排列所需要的最少交换次数等于排列的逆序数，交换次数的奇偶性和排列的奇偶性相同。

定义排列的概念后，$n$阶行列式可以作如下定义：

$$
\boxed{
\begin{aligned}
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix} = \sum_{j_1j_2\cdots j_n}(-1)^{\mathrm r(j_1j_2\cdots j_n)}a_{1j_1}a_{2j_2}\cdots a_{nj_n}
\end{aligned}}
$$

其中：

1. $j_1j_2\cdots j_n$为$1, 2, \cdots, n$组成的一组排列，等式右侧对所有可能的排列进行求和
2. 函数$\mathrm r(j_1j_2\cdots j_n)$定义为计算一个排列的逆序数

## 1.2 行列式的性质

根据行列式的计算规则，行列式具有如下性质：

> **定义** 形如下式的行列式称为上三角行列式，即$(\forall i)(\forall j)(j< i\rightarrow a_{ij} = 0)$
> $\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\   0      & a_{22} & \cdots & a_{2n} \\   \vdots & \vdots & \ddots & \vdots \\   0      & 0      & \cdots & a_{nn} \\  \end{vmatrix}$  
> 同理可以定义下三角行列式为各元素$a_{ij}$满足$(\forall i)(\forall j)(j> i\rightarrow a_{ij} = 0)$的行列式。

上三角行列式是结构较为简单的行列式：

> **定理2.1** 上三角行列式等于主对角线上元素的乘积，即：
> $\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 0      & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0      & 0      & \cdots & a_{nn} \\ \end{vmatrix} = a_{11}a_{22}\cdots a_{nn} = \prod _{i=1}^na_{ii}$

特殊地，对角行列式（除主对角线元素以外其余元素均为0的行列式）等于主对角线上元素的乘积。

以下不加证明地给出行列式的部分性质：

> **定理2.2** 转置操作不改变行列式的值，即  
> $\begin{vmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{vmatrix} = \begin{vmatrix} a_{11} & a_{21} & \cdots & a_{n1} \\ a_{12} & a_{22} & \cdots & a_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n} & a_{2n} & \cdots & a_{nn} \end{vmatrix}$
>
> **定理2.3** 若行列式的某行（或某列）有公因子时，该公因子可以提取出行列式，即：  
> $\begin{vmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\\vdots & \vdots &        & \vdots \\ka_{p1} & ka_{p2} & \cdots & ka_{pn} \\\vdots & \vdots &        & \vdots \\a_{n1} & a_{n2} & \cdots & a_{nn}\end{vmatrix} = k\begin{vmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\\vdots & \vdots &        & \vdots \\a_{p1} & a_{p2} & \cdots & a_{pn} \\\vdots & \vdots &        & \vdots \\a_{n1} & a_{n2} & \cdots & a_{nn}\end{vmatrix}$
>
> **定理2.4** （ **定理2.3** 推论）若行列式的某行（或某列）全为0，则行列式为0  
> 
> **定理2.5** （ **定理2.3** 推论）若行列式的某两行（列）成比例，则行列式为0
>
> **定理2.6** 行列式可以按下式分为两个行列式之和
> $\begin{vmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\\vdots & \vdots &        & \vdots \\a_{p1} + a'_{p1} & a_{p2} + a'_{p2} & \cdots & a_{pn} + a'_{pn} \\\vdots & \vdots &        & \vdots \\a_{n1} & a_{n2} & \cdots & a_{nn}\end{vmatrix} = \begin{vmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\\vdots & \vdots &        & \vdots \\a_{p1} & a_{p2} & \cdots & a_{pn} \\\vdots & \vdots &        & \vdots \\a_{n1} & a_{n2} & \cdots & a_{nn}\end{vmatrix} + \begin{vmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\\vdots & \vdots &        & \vdots \\a'_{p1} & a'_{p2} & \cdots & a'_{pn} \\\vdots & \vdots &        & \vdots \\a_{n1} & a_{n2} & \cdots & a_{nn}\end{vmatrix}$  
>
> **定理2.7** 对换行列式中两行的位置，行列式反号  
>
> **定理2.8** （ **定理2.5、定理2.6** 推论）将一行（列）的某个倍数加到另一行（列），行列式的值不变

## 1.3 行列式的展开

> **定义** 对于行列式$B=|b_{ij}|_n$，定义行列式$M_{ij}$为$B$划去第$i$行和第$j$列剩余的部分，称$M_{ij}$为$b_{ij}$的余子式，称$A_{ij} = (-1)^{i+j} M_{ij}$称为$b_{ij}$的代数余子式

根据余子式可以将行列式分解为阶数降一阶的行列式之和：

> **定理3.1** $n$阶行列式