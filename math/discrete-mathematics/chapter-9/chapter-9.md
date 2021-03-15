# 集合

集合是一些确定的、可以区分的事物汇聚在一起组成的一个整体，组成一个集合的每个事物称为该集合的一个元素。

* 集合的元素可以是任何事物，也可以是另一个集合，但不能是自身
* 集合中的元素满足唯一性，不会出现相同的元素
* 集合中的元素没有顺序关系
* 元素与集合的关系是确定的，即属于（$\in$）与不属于（$\not\in$）

## 集合的表示

以下列举出常见的集合：

* $\mathbf N$表示全体自然数组成的集合
* $\mathbf Z$表示全体整数组成的集合
* $\mathbf Q$表示全体有理数组成的集合
* $\mathbf R$表示全体实数组成的集合
* $\mathbf C$表示全体复数组成的集合

可以用外延表示法或内涵表示法表示一个集合：

* 外延表示法：一一列举出集合的全体元素
* 内涵表示法：使用谓词表述集合中元素的性质

## 集合的运算

### 集合的关系运算

集合与元素存在属于与不属于关系，记作$\in, \not\in$

集合之间可以定义关系$=, \subseteq, \subset, \supseteq, \supset$。

* $A=B\Leftrightarrow (\forall x)(x\in A\leftrightarrow x\in B)$
* $A\subseteq B\Leftrightarrow (\forall x)(x\in A\rightarrow x\in B)$
* $A\subset B\Leftrightarrow (\forall x)(x\in A\rightarrow x\in B)\land A\not =B$
* $A\supseteq B\Leftrightarrow B\subseteq A$
* $A\supset B\Leftrightarrow B\subset A$

$\subseteq, \supseteq, =$关系满足自反性、传递性，$=$关系满足对称性。

$A\subseteq B\land B\subseteq A\Leftrightarrow A=B$

定义**空集**为不含任何元素的集合，记作$\varnothing$，其内涵表示为$\varnothing = \{x|x\not= x\}$，空集满足如下性质：

* 空集是任何集合的子集
* 空集是唯一的

定义**全集**为所有事物的集合，记作$E$，其内涵表示为$E=\{x|x=x\}$

### 集合的基本运算

集合包含如下基本运算：

* 并集：$A\cup B = \{x\in A\lor x\in B\}$
* 交集：$A\cap B = \{x\in A\land x\in B\}$
* 差集：$A-B = \{x\in A\land x\not \in B\}$
* 补集：$-A=E-A=\{x|x\not\in A\}$
* 对称差：$A\oplus B=(A-B)\cup (B-A) = \{x| x\in A\overline\lor x\in B\}$

基于并集与交集运算可以拓展出广义并和广义交的概念，设集合$A$的所有元素都是集合，定义$A的广义并、广义交如下：

* 广义并：$\cup A=\{x| (\exists z)(z\in A\land x\in z)\}$
* 广义交：$\cap A=\{x| (\forall z)(z\in A\rightarrow x\in z)\}$

即：集合$A$的广义并是集合中所有元素的并集，集合$A$的广义交是集合中所有元素的交集。

定义**幂集**为集合所有子集（包括自身）组成的集合，记作$P(A)$

定义笛卡尔积$A\times B$为二元组（有序对）$\langle x, y\rangle$的集合，其中$x\in A, y\in B$。有序对的定义不一定唯一，如集合$\{x, \{x, y\}\}$即可表示一个有序对。有序对满足如下性质：

* $x\not = y\Rightarrow \langle x,y\rangle \not =\langle y,x\rangle$
* $\langle x,y\rangle = \langle u,v\rangle\Leftrightarrow x=u\land y=v$

可以在二元组的基础上拓展$n$元组的定义：$\langle x_1, \dots, x_n\rangle =\langle\dots\langle x_1, x_2\rangle, \dots, x_n\rangle$。由此$n$阶笛卡尔积$A_1\times A_2\times\dots\times A_n$即为$\{\langle x_1, \dots, x_n\rangle|x_1\in A_1\land \dots\land x_n\in A_n\}$

### 集合运算的优先级

集合运算的优先级列举如下：

$$
\begin{aligned}
    &-A, P(A), \cap A, \cup A \\
    &-, \cap, \cup, \oplus, \times \\
    &=, \subseteq , \subset, \in \\
    &\lnot \\
    &\land, \lor, \rightarrow, \leftrightarrow \\
    &\Leftrightarrow, \Rightarrow
\end{aligned}
$$

### 集合运算的性质

集合的基本运算满足如下性质：

1. 交换律
   1. $A\cap B=B\cap A$
   2. $A\cup B=B\cup A$
2. 结合律
   1. $(A\cup B)\cup C = A\cup (B\cup C)$
   2. $(A\cap B)\cap C = A\cap (B\cap C)$

## 集合的图示法

* 对于集合的基本运算，可以使用文氏图表示
* 对于幂集运算，可以使用网络图表示
* 对于笛卡尔积运算，可以使用二维坐标系表示