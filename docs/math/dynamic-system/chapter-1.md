# 古典控制理论概述

一个系统可以通过三种方式进行描述，即：

1. 状态方程
2. 微（差）分方程
3. 传递函数

借助于 Laplace 变换，可以将微分方程描述的系统转变为传递函数描述。

!!! note "Laplace 变换"
    > **定义：** 对于定义域包含$[0, +\infty)$的函数$f(t)$，$f(t)$的 Laplace 变换用$\mathcal {L[f(t)](s)}$表示，有：
    >
    > $$
    \mathcal {L}[f(t)](s) = \frac {1}{s} \int_{0}^{\infty} f(t) e^{-st} dt, s=\sigma + j\omega \in \mathbb C
    $$
    >
    > 若该积分存在，则$f(t)$的 Laplace 变换存在。

    通常地，满足下列条件的函数，存在 Laplace 变换：

    1. $f(t)$在$[0, +\infty)$的有限个子区间$t\in [t_1, T], t_1 \geq 0$上连续或分段连续。
    2. $f(t)=0, \forall t<0$
    3. $\forall s_{0}, \exists d, \forall t, e^{-s_0t}|f(t)| < d$

    Laplace 变换满足如下性质：

    * 线性变换

    $$
    \mathcal {L}[Af_{1}(t) + Bf_{2}(t)](s) = A\mathcal {L}[f_{1}(t)](s) + B\mathcal {L}[f_{2}(t)](s)
    $$

    * 微分定理
      
    $$
    \mathcal {L}\left[\frac{\mathrm d^nf}{\mathrm dt^n}(t)\right](s) = s\mathcal{L}[f(s)] - \left[s^{n-1}f(0) + \sum_{i=1}^{n-1}\left(s^{n-1-i}\frac{\mathrm d^{i}f}{\mathrm dt^{i}}\left| _{t=0}\right.\right)\right]
    $$

    * 积分定理

    $$
    \mathcal L\left[\int _0^t f(\tau)\mathrm d\tau\right] = \frac{F(s)}s + \frac{f^{-1}(0)}{s}
    $$

    其中$f^{-1}(0) = \int_{0}^tf(\tau)\mathrm d\tau$在$t=0$时的值。

    * 初值定理

    

    * 终值定理