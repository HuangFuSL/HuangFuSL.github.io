# 对偶

## 拉格朗日对偶函数

$$
\optim{\min}{f_0(x)}{\cases{\begin{aligned}
    & f_i(x)\leq 0 & i = \oneto m \\
    & h_i(x) = 0 & i = \oneto p
\end{aligned}}}
\label{1}
$$

对于一个形如$\eqref{1}$的优化问题（不一定是凸优化问题），其**拉格朗日函数**为$L: \bbR^n\times \bbR^m\times \bbR^p$，其中$\lambda, \nu$为向量，称为**拉格朗日乘子向量**。

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_if_i(x) + \sum_{i=1}^p\nu_i h_i(x)
\label{2}
$$

$\eqref{2}$关于$x$的最小值$g(\lambda, \nu)$称为**拉格朗日对偶函数**。

$$
g(\lambda, \nu) = \inf_{x\in \calD}\left(f_0(x) + \sum_{i=1}^m \lambda_if_i(x) + \sum_{i=1}^p\nu_i h_i(x)\right)
\label{3}
$$

拉格朗日对偶函数是原问题最优值的下界：$\forall \lambda \succeq 0, \forall \nu, g(\lambda, \nu)\leq p^*$，并且是凹函数。拉格朗日对偶函数可以由目标函数$f_0$的共轭函数表示。

## 拉格朗日对偶问题

记$\eqref{1}$的**（拉格朗日）对偶问题**为：

$$
\optim{\max}{g(\lambda, \nu)}{\lambda \succeq 0}
$$

其最优解$(\lambda^*, \nu^*)$称为其对偶最优解。拉格朗日对偶问题是凸优化问题。

!!! theorem "标准线性规划的对偶问题"

    考虑标准形式的线性规划问题

    $$
    \optim{\min}{c^\top x}{\cases{\begin{aligned}
        & Ax = b \\
        & x\succeq 0
    \end{aligned}}}
    $$

    拉格朗日对偶函数为

    $$
    \begin{aligned}
        g(\lambda, \nu) &= \inf_{x}(c^\top x - \lambda^\top x + \nu^\top (Ax - b)) \\
        &= \inf_{x}(-\nu^\top b + (c - \lambda + A^\top \nu)^\top x) \\
        &= \cases{\begin{aligned}
            & -\nu^\top b & c - \lambda + A^\top\nu = 0 \\
            & -\infty & \otherwise
        \end{aligned}}
    \end{aligned}
    $$

    因此，拉格朗日对偶问题为

    $$
    \optim{\max}{\nu^\top b}{\cases{\begin{aligned}
        & c - \lambda + A^\top \nu = 0 \\
        & \lambda \succeq 0
    \end{aligned}}}
    $$

    即

    $$
    \optim{\max}{\nu^\top b}{
        c + A^\top \nu \succeq 0
    }
    $$

    线性规划问题对偶问题的对偶等价于原问题。

### 弱对偶性

记对偶问题的最优值为$d^*$。根据对偶函数的性质，有$d^*\leq p^*$，此为**弱对偶性**。

* 若原问题无下界，则$p^* = -\infty$，此时有$d^* = -\infty$，即对偶问题不可行。
* 若对偶问题无上界，则$d^* = \infty$，此时$p^* = \infty$，即原问题不可行。

记$p^* - d^*\geq 0$为**对偶最优间隙**。

### 强对偶性

**强对偶性**即$p^* - d^* = 0$。强对偶性并不是总成立，需要对凸优化问题施加**约束准则**。

若（任意）凸优化问题满足**Slater条件**，即$\exists x\in \mathbf{relint} \calD$使得约束条件严格成立，即

$$
\cases{\begin{aligned}
    & f_i(x)\leq 0 & i = \oneto m \\
    & Ax = b
\end{aligned}}
$$

时，强对偶性成立。

如果原问题中的某个不等式约束是线性的，则这个约束不需要满足严格成立的条件。

### 几何解释

设集合$\calG = \{(f_1(x), \ldots, f_m(x), h_1(x), \ldots, h_p(x), f_0(x))\in \bbR^m\times \bbR^p\times\bbR | x\in \calD\}$，则优化问题的最优值为

$$
p^* = \inf_t\{(u, v, t)\in \calG | u\preceq 0, v = 0\}
$$

拉格朗日对偶函数可以表示为$g(\lambda, \nu) = \inf\{ (\lambda, \nu, 1)^\top (u, v, t) | (u, v, t)\in \calG\}\leq (\lambda, \nu, 1)^\top (u, v, t)$，定义了一个超平面，其法向量为$(\lambda, \nu, 1)$，与直线$u=v=0$相交于$(0, 0, g(\lambda, \nu))$。也即，每个对偶问题的解都是集合$\calG$的一个支撑超平面。

定义$\calG$的上境图$\calA = \calG + \bbR_\plus^m\times\{0\}^p\times \bbR_\plus$，即

$$
\calA = \{(u_0 + x, v_0, t_0 + z) | (u_0, v_0, t_0)\in \calG, x\in \bbR_\plus^m, z\in \bbR_\plus\}
$$

则对应的原问题最优值为

$$
p^* = \inf\{t | (0, 0, t)\in \calA\}
$$

强对偶性成立当且仅当$\calA$中存在一组$(u, v, t)\in \mathbf{bd}\calA$使得在该处的支撑超平面与坐标轴$u=v=0$相交于$(0, 0, p^*)$，也即当且仅当$\calA$是凸集。

### 最大最小解释

设$p = 0$。则原问题可以写作如下形式的无约束优化问题：

$$
\optim{\min}{\sup_{\lambda\succeq 0}L(x, \lambda)}{x\in \bbR^n}
$$

对偶问题可以写作如下形式的优化问题：

$$
\optim{\max}{\inf_{x} L(x, \lambda)}{\lambda\succeq 0}
$$

因此弱对偶性可以写作

$$
\sup_{\lambda\succeq 0}\inf_{x}L(x, \lambda) \leq \inf_{x}\sup_{\lambda\succeq 0}L(x, \lambda)
$$

强对偶性可以写作

$$
\sup_{\lambda\succeq 0}\inf_{x}L(x, \lambda) = \inf_{x}\sup_{\lambda\succeq 0}L(x, \lambda)
$$

即$L(x, \lambda)$满足**鞍点性质**。

## 最优性条件

如果对偶问题存在一个可行解$(\lambda, \nu)$，则说明原问题的最优值满足$p^*\geq g(\lambda, \nu)$。此时对于一个可行解$x$，$x$是一个$\varepsilon = f_0(x) - g(\lambda, \nu)$-次优解。称此处的$f_0(x) - g(\lambda, \nu)$为**对偶间隙**。

原问题和对偶问题的最优值满足

$$
p^*\in [g(\lambda, \nu), f_0(x)]\qquad d^*\in [g(\lambda, \nu), f_0(x)]
$$

可以直接得出推论：若$f_0(x) = g(\lambda, \nu)$，则有$p^*=d^*=f_0(x)$

### 互补松弛性

当强对偶性成立时，互补松弛性指对于原问题最优解$x^*$及对偶问题最优解$\lambda^* = (\lambda_1^*, \ldots, \lambda_m^*)$，满足

$$
\lambda_i^* > 0 \Lora f_i(x^*) = 0
$$

即对偶最优解中的非零分量对应原问题中的紧约束。

### KKT最优条件

设原问题的目标函数和约束条件均可微，$x^*$为原问题最优解，$\lambda^*, \nu^*$为对偶问题最优解，且强对偶性成立，则拉格朗日函数$L(x, \lambda^*, \nu^*)$在$x^*$处取得最小值，则

$$
\nabla L(x^*, \lambda^*, \nu^*) = 0
$$

综合其它约束条件，可以得到KKT最优条件。

$$
\cases{
\begin{aligned}
    f_i(x^*) & \leq 0 & \text{（不等式约束）} \\
    h_i(x^*) & = 0 & \text{（等式约束）} \\
    \lambda_i^* & \geq 0 & \text{（对偶问题约束）} \\
    \lambda_i^* f_i(x^*) &= 0 & \text{（互补松弛性）} \\
    \nabla L(x^*, \lambda^*, \nu^*) &= 0 & \text{（最优条件）}\\
\end{aligned}
}
$$

对于任意优化问题，若强对偶性成立，则最优解必须满足KKT条件（反过来不一定成立）。对于满足强对偶性的凸优化问题，满足KKT条件的点是原问题和对偶问题的最优解。

## 广义不等式约束的对偶问题

设原问题为

$$
\optim{\min}{f_0(x)}{\cases{
    \begin{aligned}
        & f_i(x)\preceq_{K_i} 0 \\
        & h_i(x) = 0
    \end{aligned}
}}
$$

拉格朗日函数为

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i^\top f_i(x) + \sum_{j=1}^p \nu_j^\top h_j(x)
$$

对偶问题为

$$
\optim{\max}{g(\lambda, \nu) = \inf_{x}L(x, \lambda, \nu)}{\lambda_i\succeq_{K_i^*}0}
$$

在广义不等式下，弱对偶性总是成立。满足（广义）Slater条件$\eqnref{4}$时，强对偶性成立。

$$
\forall i=1,\ldots, m,\exists x\in \mathbf{relint}\calD, Ax=b, f_i(x)\prec_{K_i}0
\label{4}
$$

强对偶性成立时，互补松弛性和KKT条件成立。
