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