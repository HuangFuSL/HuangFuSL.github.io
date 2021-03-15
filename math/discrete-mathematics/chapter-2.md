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

### 从值为T的行生成

对于包含$n$个命题变元$P_1, \dots, P_n$的命题公式，写出如下合取式：

$$
P_1\land P_2\land \dots \land P_n
$$

对于真值表的每个取值为$T$的行，若对应的$P_i$为$F$，则将合取式中的对应$P_i$替换为$\lnot P_i$。将所得的公式使用析取运算符连接即得符合真值表的命题公式。

### 从值为F的行生成

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

## 对偶式

设$A$为命题公式，将$A$中出现的$\lor, \land, T, F$分别使用$\land, \lor, F, T$进行替换，所得到的公式称为$A$的对偶式，记为$A^*$

设$A$为命题公式，将$A$中出现的所有命题变项$P_1,\dots, P_n$替换为$\lnot P_1, \dots, \lnot P_n$，所得到的公式称为$A$的否命题，记为$A^-$

则取对偶式运算、取否命题运算有如下性质：

1. $\lnot (A^*) = (\lnot A)^*, \lnot (A^-) = (\lnot A)^-$
2. $(A^*)^*=A, (A^-)^- =A$
3. $A^{*-}=\lnot A$
4. $A=B\Rightarrow A^*=B^*$
5. 对$A\rightarrow B$取对偶式可得$A\rightarrow B=T\Rightarrow B^*\rightarrow A^*=T$

***

根据对偶式和否命题的定义，2式自然成立。1式和3式可以通过数学归纳法进行证明。

## 范式

定义如下概念：

* 文字：简单命题$P$及其否定形式
* 合取式：一些文字的合取，形如$P_1\land \dots \land P_n$
* 析取式（子句）：一些文字的析取，形如$P_1\lor \dots\lor P_n$
* 互补对：文字与其对应的否定形式
* 析取范式：合取式通过析取联结词连接的公式，形如$A_1\lor \dots\lor A_n$，其中$A_i$为合取式
* 合取范式：析取式通过合取联结词连接的公式，形如$A_1\land \dots \land A_n$，其中$A_i$为析取式

由此，可以导出范式定理，即任一命题公式都存在有与之等值的合取范式与析取范式。范式定理的正确性可以通过列写命题公式的真值表与从真值表列写命题公式证明。

计算合取范式与析取范式：

1. 消去逻辑联结词$A\rightarrow B$与$A\leftrightarrow B$，替换为$\lnot A\lor B$与$(\lnot A\lor B)\land (A\lor \lnot B)$
2. 使用摩根律与双重否定律消除$\lor$或$\land$，并消除多余的$\lnot$
3. 将所有的$\lnot$移动到命题变项$P_i$前
4. 使用分配律将公式化为范式

### 主范式

对于公式$Q = Q_1\land \dots \land Q_n$，式中$Q_i=P_i$或$Q_i=\lnot P_i$。则$Q$为**极小项**，记为$m_i$。

* 极小项中必须出现所有的命题变项
* $n$个命题变项可以组成$2^n$个极小项，依次表示为$m_1, \dots m_{2^n}$

对于公式$R = R_1\lor \dots \lor R_n$，式中$R_i = P_i$或$R_i = \lnot P_i$。则$R$为**极大项**，记为$M_i$

与极小项相同，所有的命题变项必须都出现在极大项中，且$n$个命题变项可以组成$2^n$个极大项。

任意公式$A$的范式中，仅由极小项构成的析取范式为主析取范式，仅由极大项构成的合取范式为主合取范式。主析取范式与主合取范式都是唯一的。

极大项、极小项满足如下性质

1. 极大项、极小项的数量等于公式可能的解释数量，即$2^n$
2. 每个极小项仅在公式的一个解释下为$T$，每个极大项仅在公式的一个解释下为$F$
3. 极小项、极大项两两不等值，有$m_i\land m_j\leftrightarrow i=j, M_i\lor M_j\leftrightarrow i\not= j$。
4. 任一含有$n$个命题变项的公式都可以用$k\leq n$个极小项或$k\leq n$个极大项表示。
5. $\bigwedge _{i=0} ^{2^n-1} M_i=F, \bigvee _{i=0}^{2^n-1} m_i = T$

## 推理形式

将自然语句描述的推理关系经抽象化后使用条件式的表示

若$A\rightarrow B=T$，称$A$重言蕴含$B$，记作$A\Rightarrow B$。重言蕴含关系具有如下性质：

1. 若$A=T$，且$A\Rightarrow B$，则$B=T$
2. 若$A\Rightarrow B\land B\Rightarrow A$，则$A=B$
3. 若$A\Rightarrow B\land B\Rightarrow C$，则$A\Rightarrow C$
4. 若$A\Rightarrow B\land A\Rightarrow C$，则$A\Rightarrow (B\land C)$
5. 若$A\Rightarrow C\land B\Rightarrow C$，则$(A\lor B)\Rightarrow C$

要证明一个式子为重言蕴含式，可以证明$A\rightarrow B$为重言式或$\lnot A\land B$为矛盾式。

### 基本的推理公式

如下列出一些基本的推理公式，式中$P,Q,R,S$均为任意命题变项

* $P\land Q\Rightarrow P$
* $\lnot(P\rightarrow Q)\Rightarrow P$
* $\lnot(P\rightarrow Q)\Rightarrow \lnot Q$
* $P\Rightarrow P\lor Q$
* $\lnot P\Rightarrow P\rightarrow Q$
* $Q\Rightarrow P\rightarrow Q$
* $\lnot P \land(P\lor Q)\Rightarrow Q$
* $P\land (P\rightarrow Q) \Rightarrow Q$，分离规则
* $\lnot Q\land (P\rightarrow Q)\Rightarrow \lnot P$
* $(P\rightarrow Q)\land (Q\rightarrow R)\Rightarrow P\rightarrow R$，三段论
* $(P\leftrightarrow Q)\land (Q\leftrightarrow R)\Rightarrow P\leftrightarrow R$
* $(P\rightarrow R)\land (Q\rightarrow R)\land (P\lor Q)\Rightarrow R$
* $(R\rightarrow Q)\land (R\rightarrow S)\land (P\lor R)\Rightarrow Q\lor S$
* $(P\rightarrow Q)\land (R\rightarrow S)\land (\lnot Q\lor \lnot S)\Rightarrow (\lnot P\lor \lnot R)$
* $Q\rightarrow R\Rightarrow ((P\lor Q)\rightarrow (P\lor R))$
* $Q\rightarrow R\Rightarrow ((P\rightarrow Q)\rightarrow (P\rightarrow R))$

### 推理演算

推理演算过程中，有如下规则可以使用：

* 前提引入规则：推理过程中可以随时引入前提
* 结论引用规则：推理过程中的中间结论可以作为后续推理的前提
* 代入规则：推理过程中对重言式的命题变项可以使用代入规则
* 置换规则：推理过程中任何部分都可以用与之等值的命题公式进行替换
* 分离规则：若$A$且$A\rightarrow B$则$B$
* 条件证明规则：$A_1\land A_2\Rightarrow B \Leftrightarrow A_1\Rightarrow A_2\rightarrow B$

### 归结推理

思路：要证明$A\Rightarrow B$，可证明$A\land \lnot B=F$。

* 将$C = A\land \lnot B$化为合取范式$Q_1\land \dots \land Q_n$，式中的所有析取式构成子句集合$\{Q_1,\dots, Q_n\}$
* 消去子句集合中的互补对，如$P\lor R$与$\lnot P\lor \lnot Q$归结得到$R\lor \lnot Q$。不断重复消去过程。
* 直到子句集合为空，得到空子句$\square$，证明$A\land \lnot B$是矛盾式