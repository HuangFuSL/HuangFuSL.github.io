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
> **定义：** 对于一个$n$阶排列$a_1, \dots, a_n$，定义该排列的逆序数等于排列中逆序对的个数。称逆序数为奇数的排列为奇排列，逆序数为偶数的排列为偶排列，逆序数为0的排列为自然排列。

对于排列，有如下结论：

> **定理1.1** 对换排列中的任意两个元素，排列的奇偶性改变；  
> **定理1.2** 奇排列的个数与偶排列的个数相等；  
> **定理1.3** 可以通过有限次对换操作将任何排列转变为自然排列  

根据逆序数的定义、定理1.1与定理1.3，可以推出如下结论：

> **定理1.4** 将任意排列转变为自然排列所需要的最少交换次数等于排列的逆序数，交换次数的奇偶性和排列的奇偶性相同。
