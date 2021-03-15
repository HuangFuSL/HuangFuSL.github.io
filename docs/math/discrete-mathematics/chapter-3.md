# 命题逻辑的公理化

公理系统包含如下结构：

* 初始符号：定义了公理系统中允许出现的符号集合
* 形成规则：定义了符号序列的合法性
* 公理：公理系统中最基本的重言式，是推演其他所有重言式的依据
* 变形规则：公理系统所规定的推演规则，公理通过变形规则得到的公式为重言式，称为定理

## 命题逻辑的公理系统

依据公理系统的结构建立命题逻辑的公理系统。应当注意到，命题逻辑的公理系统不是唯一的。

### 初始符号

大写英文字母$A,\dots ,Z$表示命题  
$\lnot, \lor$表示联结词  
$(, )$一对括号规定了联结词运算的优先顺序  
$\vdash$表明一个公式是永真式

### 形成规则

称初始符号构成的符号序列为公式，只有符合以下条件的符号序列是合式公式：

1. 单个符号$\pi$，$\pi$是大写英文字母
2. 若$A$为合式公式，$\lnot A$是合式公式
3. 若$A, B$为合式公式，$(A\lor B)$是合式公式

为简化其他合式公式的表达，引入如下所示的公式：

* $(A\rightarrow B):= (\lnot A\lor B)$
* $(A\land B):= \lnot (\lnot A\lor \lnot B)$
* $(A\leftrightarrow B):= ((A\rightarrow B)\land (B\rightarrow A))$

### 公理

在公理系统中引入如下公理：

* $\vdash ((P\lor P)\rightarrow P)$
* $\vdash (P\rightarrow (P\lor Q))$
* $\vdash ((P\lor Q) \rightarrow (Q\lor P))$
* $\vdash ((Q\rightarrow R)\rightarrow ((P\lor Q)\rightarrow (P\lor R)))$

### 推理规则

代入规则、分离规则、置换规则是命题逻辑公理系统中的推理规则

## 王浩算法

### 初始符号

大写字母$A, \dots, Z$表示命题  
$\lnot, \land, \lor, \rightarrow, \leftrightarrow$表示联结词  
$(, ), ,$表示圆括号与逗号  
$\alpha, \beta, \dots, \omega$表示公式串

### 形成规则

符合以下条件的符号序列称为合式公式：

1. 单个符号$\pi$，$\pi$是大写英文字母
2. 若$A$为合式公式，则$\lnot A$为合式公式
3. 若$A, B$为合式公式，则$(A\lnot B), (A\lor B), (A\rightarrow B), (A\leftrightarrow B)$是合式公式

满足以下条件的称为公式串：

1. 空符号串是公式串
2. 合式公式是公式串
3. 如果$\alpha$和$\beta$是公式串，则$\alpha, \beta$是公式串

公式串与组成公式串的合式公式的顺序无关。

### 定义

1. 定义**相继式**为$\alpha\stackrel s\rightarrow\beta$，其中$\alpha, \beta$都是公式串
2. 前件中的$,$解释为$\land$，后件中的$,$解释为$\lor$
3. 若$\alpha\stackrel s\rightarrow \beta$为重言式，可以记作$\alpha\stackrel s\Rightarrow \beta$

### 公理

若$\alpha$和$\beta$的公式仅为命题变项，不包含联结词，则$\alpha\stackrel s\rightarrow \beta$为重言式等价于$\alpha$与$\beta$中至少含有一个相同的命题变项

### 推理规则

对于存在于前件中的运算符，推理规则如下：

* $\lnot$：若$\alpha, \beta \stackrel s\Rightarrow X, \gamma$，则$\alpha, \lnot X, \beta \stackrel x\Rightarrow \gamma$
* $\land$：若$X, Y, \alpha, \beta\stackrel s\Rightarrow \gamma$，则$\alpha, X\land Y, \beta\stackrel s\Rightarrow Y$
* $\lor$：若$X, \alpha, \beta \stackrel s\Rightarrow \gamma$且$Y, \alpha, \beta \stackrel s\Rightarrow X, \gamma$，则$\alpha, X\lor Y, \beta\stackrel s\Rightarrow \gamma$
* $\rightarrow$：若$Y, \alpha, \beta\stackrel s\Rightarrow \gamma$且$\alpha, \beta\stackrel s\Rightarrow X, \gamma$，则$\alpha, X\rightarrow Y, \beta\stackrel s\Rightarrow \gamma$
* $\leftrightarrow$：若$X, Y, \alpha, \beta\stackrel s\Rightarrow \gamma$且$\alpha, \beta\stackrel s\Rightarrow X, Y, \gamma$，则$\alpha, X\leftrightarrow Y, \beta\stackrel s\Rightarrow \gamma$

对于存在于后件中的运算符，推理规则如下：

* $\lnot$：若$X, \alpha\stackrel s\Rightarrow \beta, \gamma$，则$\alpha\stackrel s\Rightarrow\beta, \lnot X, \gamma$
* $\land$：若$\alpha\stackrel s\Rightarrow X, \beta, \gamma$且$\alpha\stackrel s\Rightarrow$
* $\land$：若$\alpha\stackrel s\Rightarrow X, \beta, \gamma$且$\alpha\stackrel s\Rightarrow Y, \beta, \gamma$，则$\alpha \stackrel s\Rightarrow\beta, X\land Y, \gamma$
* $\lor$：若$\alpha\stackrel s\Rightarrow X, Y, \beta, \gamma$，则$\alpha\stackrel s\Rightarrow \beta, X\lor Y, \gamma$
* $\rightarrow$：若$X, \alpha\stackrel s\Rightarrow Y, \beta, \gamma$，则$\alpha\stackrel s\Rightarrow \beta, X\rightarrow Y, \gamma$
* $\leftrightarrow$：若$X, \alpha\stackrel s\Rightarrow Y, \beta, \gamma$且$Y, \alpha\stackrel s\Rightarrow X, \beta, \gamma$，则$\alpha \stackrel s\Rightarrow \beta, X\leftrightarrow Y, \gamma$

定理的推演过程：

1. 将要证明的定理写成相继式形式
2. 从相继式出发使用变形规则消去相继式两侧的所有逻辑联结词
3. 若得到的所有相继式都是公理，则定理成立

## 命题逻辑的自然演绎系统

### 初始符号

命题逻辑的自然演绎系统的一部分初始符号继承自命题逻辑的公理系统。此外，命题逻辑的自然演绎系统还包含如下初始符号：

$$
\varGamma = \{A_1, \dots, A_n\}=A_1, \dots, A_n
$$

表示有限个命题公式集合，定义$\varGamma \vdash A$表示$\varGamma, A$之间有形式推理关系，$\varGamma$为形式前提，$A$为形式结论。

### 形成规则

命题逻辑的自然演绎系统的形成规则与命题逻辑的公理系统的形成规则相同

### 变形规则

命题逻辑的自然演绎系统有如下变形规则：

1. $A_1, \dots, A_n\vdash A_i(i=1, \dots, n)$，即前提中的任何命题都可以作为结论出现
2. 传递律：若$\varGamma \vdash A$且$A\vdash B$，则$\varGamma\vdash B$
3. 反证律：若$\varGamma, \lnot A\vdash B$且$\varGamma, \lnot A\vdash \lnot B$，则$\varGamma \vdash A$（等价于证明$\varGamma \land \lnot A=F$）
4. 分离规则：$A, A\rightarrow B\vdash B$
5. 蕴含词引入：若$\varGamma, A\vdash B$，则$\varGamma\vdash A\rightarrow B$

### 定理

命题逻辑的自然演绎系统包含的定理与命题逻辑的公理系统包含的定理相同

## 非标准逻辑

1. 多值逻辑，若$P$取值于$[0,1]$，可以解释为
    * $P=0$表示$P$真
    * $P=1$表示$P$假
    * $0<P<1$表示$P$为真的概率为$1-P$ 
2. 三值逻辑
    * Kleene逻辑：$T, F, U$，$U$表示未知
    * Lukasiewicz逻辑：$T, F, I$，$I$表示将来可能，目前不具备真值
    * Bochvar逻辑：$T, F, M$，$M$表示悖论