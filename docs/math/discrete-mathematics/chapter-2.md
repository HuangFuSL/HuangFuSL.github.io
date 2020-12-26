# 命题逻辑的等值和推理演算

等值：设$A, B$为公式，$P_1, \dots, P_n$是出现在$A, B$中所有的命题变项，若对于任意的一组$\left\langle P_1, \dots, P_n\right\rangle$，都有$A=B$，则称公式$A$与公式$B$等值（等价），记为$A\Leftrightarrow B$或$A=B$。

等值关系满足自反性、对称性与传递性：

* $A=A$
* 若$A=B$，则$B=A$
* 若$A=B, B=C$，则$A=C$

$A=B$的充分必要条件是$A\leftrightarrow B$为重言式。

## 等值公式

基本的等值公式列举如下：

* 双重否定律
  * $P = \lnot \lnot P$
* 结合律
  * $(P\lor Q)\lor R = P \lor (Q\lor R)$
  * $(P\land Q)\land R = P \land (Q\land R)$
  * $(P\leftrightarrow Q)\leftrightarrow R = P \leftrightarrow (Q\leftrightarrow R)$
  * 运算符$\rightarrow$不满足结合律
* 交换律
  * $P\lor Q = Q\lor P$
  * $P\land Q = Q\land P$
  * $P\leftrightarrow Q = Q\leftrightarrow P$
  * 运算符$\rightarrow$不满足交换律
* 分配律
  * $P\lor (Q\land R) = (P\lor Q)\land (P\lor R)$
  * $P\land (Q\lor R) = (P\land Q)\lor (P\land R)$
  * $P\rightarrow (Q\rightarrow R) = (P\rightarrow Q)\rightarrow (P\rightarrow R)$
  * 运算符$\leftrightarrow$不满足分配律
* 恒等律
  * $P\lor P = P$
  * $P\land P = P$
  * $P\rightarrow P = T$
  * $P\leftrightarrow P = T$
* 吸收率
  * $P\lor (P\land Q) = P$
  * $P\land (P\lor Q) = P$
* 摩根律
  * $\lnot (P\lor Q) = \lnot P\land \lnot Q$
  * $\lnot (P\land Q) = \lnot P\lor \lnot Q$
  * $\lnot (P\rightarrow Q) = P\land \lnot Q$
  * $\lnot (P\leftrightarrow Q) = (P\land \lnot Q) \lor (\lnot P\land Q)$
* 同一律
  * $P\lor F = P$
  * $P\land P = T$
  * $T\rightarrow P = P$
  * $T\leftrightarrow P = P$
  * $P\rightarrow F = \lnot P$
  * $P\leftrightarrow F = \lnot P$
* 零律
  * $P\lor T = T$
  * $P\land F = F$
  * $P\rightarrow T = T$
  * $F\rightarrow P = T$
* 补余律
  * $P\lor \lnot P = T$
  * $P\land \lnot P = F$
  * $P\rightarrow \lnot P = \lnot P$
  * $P\leftrightarrow \lnot P = F$
* 其他常用的等值公式
  1. $P\rightarrow Q = \lnot Q\rightarrow \lnot P$（逆否命题）
  2. $P\rightarrow (Q\rightarrow R) = (P\land Q)\rightarrow R$
  3. $(P\rightarrow R)\land (Q\rightarrow R) = (P\lor Q) \rightarrow R$

由公式2的直接推论：$P\rightarrow (Q\rightarrow R) = Q\rightarrow (P\rightarrow R)$

置换：对公式$A$的子公式$B$，使用与之等值的公式进行代换称为置换

设置换后的公式为$C$，则必有$A=C$

## 从真值表计算生成命题公式

从真值表生成命题公式有两种方法，既可以通过值为$T$的行生成，也可以通过值为$F$的行生成

### 从值为$T$的行生成

对于包含$n$个命题变元$P_1, \dots, P_n$的命题公式，写出如下合取式：

$$
P_1\land P_2\land \dots \land P_n
$$

对于真值表的每个取值为$T$的行，若对应的$P_i$为$F$，则将合取式中的对应$P_i$替换为$\lnot P_i$。将所得的公式使用析取运算符连接即得符合真值表的命题公式。

### 从值为$F$的行生成

对于包含$n$个命题变元$P_1, \dots, P_n$的命题公式，写出如下析取式：

$$
P_1\lor P_2\lor \dots \lor P_n
$$

对于真值表的每个取值为$F$的行，若对应的$P_i$为$T$，则将析取式中的对应$P_i$替换为$\lnot P_i$。将所得的公式使用合取运算符连接即得符合真值表的命题公式。

### 联结词的完备集

设集合$A$为由联结词组成的集合，若任意命题公式都有通过命题公式使用$A$中的联结词组合而成的公式与之等值，则$A$是联结词的完备集

通过如上对真值表的分析，任何真值表都能使用$\{\land, \lor, \lnot\}$三个运算符表示出一个命题公式。假设存在一个公式$P$，不存在$\{\land, \lor, \lnot\}$组成的公式与之等值。但通过$P$的真值表可以构造出一个命题公式$Q$，则$Q$与$P$的真值表相同，$P=Q$，矛盾。因此$\{\land, \lor, \lnot\}$是完备的。

以下列出了一部分联结词的最小完备集：

* $\{\lor, \lnot\}$
* $\{\land, \lnot\}$
* $\{\uparrow\}$
* $\{\downarrow\}$
* $\{\lnot, \rightarrow\}$

如果$A$是联结词的完备集，集合$B$中的联结词可以通过组合得到与$A$中联结词等价的联结词，则$B$也是联结词的完备集。

***

证明：$\{\lor, \lnot\}$是联结词的完备集：

$$
P\land Q = \lnot (\lnot P\lor \lnot Q)
$$

***

证明：$\{\land, \lnot\}$是联结词的完备集：

$$
P\lor Q = \lnot (\lnot P\land \lnot Q)
$$

***

证明：$\{\uparrow\}$是联结词的完备集：

* 证明$\lnot P$可以仅使用$\uparrow$运算符表示：

  $$
  \begin{aligned}
  \lnot P &= \lnot (P\land P) \\
  &= P\uparrow P
  \end{aligned}
  $$

* 证明$P\land Q$可以仅使用$\uparrow$运算符表示：
  
  $$
  \begin{aligned}
  P\land Q&= \lnot \lnot (P\land Q) \\
  &= \lnot (P\uparrow Q) \\
  &= (P\uparrow Q) \uparrow (P\uparrow Q)
  \end{aligned}
  $$

***

证明：$\{\downarrow\}$是联结词的完备集：

* 证明$\lnot P$可以仅使用$\downarrow$运算符表示：
  
  $$
  \begin{aligned}
  \lnot P &= \lnot (P\lor P) \\
  &= P\downarrow P
  \end{aligned}
  $$

* 证明$P\lor Q$可以仅使用$\downarrow$运算符表示：
  
  $$
  \begin{aligned}
  P\lor Q&= \lnot \lnot (P\lor Q) \\
  &= \lnot (P\downarrow Q) \\
  &= (P\downarrow Q) \downarrow (P\downarrow Q)
  \end{aligned}
  $$

***

证明：$\{\rightarrow, \lnot\}$是联结词的完备集：

$P\lor Q = \lnot \lnot P\lor Q = \lnot P\rightarrow Q$