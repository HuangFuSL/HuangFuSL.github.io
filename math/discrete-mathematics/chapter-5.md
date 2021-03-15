# 谓词逻辑的等值和推理演算

对于两个谓词公式$A, B$，若在$A, B$的任一解释下，$A, B$都有相同的真值，即$A\leftrightarrow B$，称$A, B$等值。记为$A=B$或$A\Leftrightarrow B$。

## 等值式

1. 将谓词公式代入命题逻辑下的等值公式即可得到谓词逻辑的等值公式
2. 否定型等值式
   1. $\lnot (\forall x)P(x) = (\exists x)\lnot P(x)$
   2. $\lnot (\exists x)P(x) = (\forall x)\lnot P(x)$
3. 量词分配等值式（$q$为命题变项，$x$为变元）
   1. $(\forall x)(P(x)\lor q) = (\forall x)P(x)\lor q$
   2. $(\exists x)(P(x)\lor q) = (\exists x)P(x)\lor q$
   3. $(\forall x)(P(x)\land q) = (\forall x)P(x)\land q$
   4. $(\exists x)(P(x)\land q) = (\forall x)P(x)\land q$
4. 对$\rightarrow$的分配律
   1. $(\forall x)(P(x)\rightarrow q) = (\exists x)P(x)\rightarrow q$
   2. $(\exists x)(P(x)\rightarrow q) = (\forall x)P(x)\rightarrow q$
   3. $(\forall x)(p\rightarrow Q(x)) = p\rightarrow (\forall x)Q(x)$
   4. $(\exists x)(p\rightarrow Q(x)) = p\rightarrow (\exists x)Q(x)$
5. 量词$\forall$对$\land$、量词$\exists$对$\lor$的分配律
   1. $(\forall x)(P(x)\land Q(x)) = (\forall x)P(x) \land (\forall x)Q(x)$
   2. $(\exists x)(P(x)\lor Q(x)) = (\exists x)P(x) \lor (\exists x)Q(x)$
6. 变元易名的分配律
   1. $(\forall x)(\forall y)(P(x)\lor Q(y)) = (\forall x)P(x) \lor (\forall x)Q(x)$
   2. $(\exists x)(\exists y)(P(x)\land Q(y)) = (\forall x)P(x) \land (\forall x)Q(x)$

## 范式

若谓词公式$A$中的一切量词都位于公式的最左侧，且量词的作用域延伸到公式的末端，则称谓词公式$A$为前束范式。前束范式的一般形式如下：

$$
(Q_1x_1)\dots (Q_nx_n)M(x_1, \dots, x_n)
$$

其中$Q_i$为全称量词$\forall$或特称量词$\exists$，$M$称为母式，不含有量词。

任何谓词公式都有与之等值的前束范式，但前束范式不唯一。通过如下流程可以将谓词公式化为前束范式：

* 将谓词公式中的$\rightarrow$联结词与$\leftrightarrow$联结词消去
* 使用摩根律，将$\lnot$内移到命题变项或谓词之前
* 使用量词分配等值式将量词移动到左侧
* 使用变元易名分配等值式合并谓词

### Skolem标准型

称一个谓词公式为$\exists$前束范式当且仅当谓词公式中的存在量词都在全称量词的左边，并且可以保持公式中至少存在一个存在量词。母式中不含有任何量词，也不含自由个体变项。  
称一个谓词公式为仅保留全称量词的前束型当且仅当谓词公式中只包含全称量词而不包含存在量词。母式中不含有任何量词，也不含自由个体变项。

* 一个谓词公式$A$可以化成相应的$\exists$前束范式，$A$普遍有效当且仅当$\exists$前束范式普遍有效
* 一个谓词公式$A$可以化成相应的仅保留全称量词的前束型，$A$不可满足当且仅当仅保留全称量词的前束型不可满足