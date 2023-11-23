# 无约束优化

无约束优化是指在$\bbR^n$上最小化$f(x)$的优化问题。一般来说，$f: \bbR^n\ra \bbR$是二次可微的凸函数，且在$\mathbf{dom} f$上存在最小值$p^*$，且唯一对应一个解为$x^*$。根据最优性条件，有

$$
\nabla f(x^*) = 0
\label{1}
$$

$\eqref{1}$有两种求解方法，即迭代法求数值解或直接求解方程的解析解。在部分情况下，$\nabla f$可能难以计算，此时需要使用迭代法$\eqref{2}$。$x^{(0)}, x^{(1)}, \ldots$称为$\eqref{1}$的极小化点列。

$$
x^{(0)}, x^{(1)}, \ldots \qquad \lim_{k\ra \infty} f\left(x^{(k)}\right) = p^*
\label{2}
$$

对于迭代法，算法不会在有限时间内结束。但当$f\left(x^{(k)}\right) - p^*\leq \varepsilon$时，即可认为达到最优值，算法终止。迭代算法对初始点$x_0$有一定要求，即$f$在$x_0$处的下水平集是闭集。

## 强凸性

函数$f$如果满足一阶条件

$$
f(y)\geq f(x) + \nabla f(x)^\top (y - x) + \frac{\gamma}{2} \Vert y - x\Vert^2
\label{3}
$$

或二阶条件

$$
\nabla^2 f(x)\succeq \gamma I
\label{4}
$$

则称$f$为$\gamma$-**强凸函数**。强凸函数相较于凸函数，在最优值处有更好的性质。

???+ theorem "次优性条件"

    对于给定$x$，$\eqref{3}$是$y$的函数，对其求梯度得到

    $$
    \nabla f(y) = \nabla f(x) + \gamma(y - x)
    $$

    令$\nabla f(\tilde y) = 0$，则$\tilde y = x - \nabla f(x) / \gamma$。此时，有

    $$
    f(y)\geq f(\tilde y)\geq f(x) + \nabla f(x)^\top (\tilde y - x) + \frac{\gamma}{2} \Vert\tilde y - x\Vert^2 = f(x) - \frac{1}{2\gamma}\Vert \nabla f(x)\Vert^2
    $$

    因此，$f(x) - p^*\leq \frac{1}{2\gamma}\Vert \nabla f(x)\Vert^2$。即任何梯度足够小的点都是近似最优解。

    $$
    \Vert\nabla f(x)\Vert\leq \sqrt{2\gamma\varepsilon}\Lora f(x) - p^*\leq \varepsilon
    $$

    或

    $$
    \Vert x - x^*\Vert\leq \frac{2}{m}\Vert\nabla f(x)\Vert
    $$

    显然，$x^*$是唯一的。

在下水平集$S$上，二阶梯度$\nabla^2 f$存在上界$\Gamma I$，定义$\kappa = \Gamma / \gamma$为$\nabla^2 f(x)$的条件数。

## 下降方法

可以按照$\eqref{5}$的方法构造点列：

$$
x^{(k+1)} = x^{(k)} + t^{(k)}\Delta x^{(k)}
\label{5}
$$

其中步长$t^{(k)} > 0$，$\Delta x$为前进方向。若满足$f{(k+1)} < f{(k)}$，则点列构成一种下降方法。根据（强）凸函数的性质，$\Delta x^{(k)}$必须满足

$$
\nabla f(x^{(k)})^\top \Delta x^{(k)} < 0
$$

即前进方向必须背对梯度方向。

### 算法表述

