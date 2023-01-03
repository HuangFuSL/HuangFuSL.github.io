# 预备知识

## 可测空间、概率空间与概率测度

$\renewcommand{\geq}{\geqslant}\renewcommand{\leq}{\leqslant}$
当一个试验的结果无法预先确定时，称该实验为**随机试验**。随机试验可能出现的所有结果集合构成样本空间$\Omega$，每个可能的结果称为样本点$\omega$。$\Omega$的子集构成的集合称为**集类**$\mathcal F$。

!!! note "可测空间"

    设$\mathcal F$为由$\Omega$的某些子集构成的非空集类，若满足以下条件：

    1. 若$A\in \mathcal F$，则$A^C = \Omega - A\in \mathcal F$。
    2. 若$A_n\in \mathcal F$，则$\bigcup\limits_{n=1}^\infty A_n \in \mathcal F$

    称$\mathcal F$为**$\sigma$域**，$(\Omega, \mathcal F)$为**可测空间**。

!!! tip inline end

    若一个集合$A$中的元素可以以序列$\{a_n\}$的形式表示，即存在一个$\mathbb N_+\rightarrow A$的双射，称集合$A$为可列集。

$\sigma$域$\mathcal F$对$\cap, \cup, -$运算封闭，任何元素经过可列次运算后仍属于$\mathcal F$。

对于集类$\mathcal A$，包含$\mathcal A$的$\sigma$域的交称为$\mathcal A$生成的$\sigma$域，记作$\sigma(\mathcal A)$。如：$\sigma(\{\varnothing, A, \Omega\}) = \{\varnothing, A, A^C, \Omega\}$。特殊地，记$\mathcal B = \sigma(\{(-\infty, \alpha], \forall \alpha \in \mathbb R\})$为Borel域。Borel域解决了样本空间在$\mathbb R$上连续的问题。可以证明，$\forall a < b, [a, b]\in \mathcal B, (a, b]\in \mathcal B, [a, b)\in \mathcal B, (a, b)\in \mathcal B$。定义$\mathcal B[a, b]$为限制在$[a, b]$上的Borel域。

!!! note "概率测度与概率空间"

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

!!! note "Borel-Cantelli引理"

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