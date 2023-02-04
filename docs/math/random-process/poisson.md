# 泊松过程

$\renewcommand{\geq}{\geqslant}\renewcommand{\leq}{\leqslant}$
满足如下条件的随机过程$\{N(t), t\geq 0\}$为**时齐泊松过程**。

1. $\{N(t), t\geq 0\}$为计数过程，且$N(0) = 0$；
2. $\{N(t), t\geq 0\}$为独立增量过程；
3. $\{N(t), t\geq 0\}$具备增量平稳性，即$N(t) - N(s)$的分布仅与$t - s$有关
4. 对于充分小的$\Delta t > 0$，有

    $$
    \left\{
    \begin{aligned}
        P(N(t + \Delta t) - N(t) = 1) &= \lambda \Delta t + o(\Delta t) \\
        P(N(t + \Delta t) - N(t) \geq 2) &= o(\Delta t)
    \end{aligned}
    \right.
    $$

## 增量的概率分布

泊松过程的增量$N(t + s) - N(s)$服从参数为$\lambda t$的泊松分布，即

$$
P[N(t + s) - N(s) = k] = \frac{(\lambda t)^k}{k!}e^{-\lambda t}
$$

???+ proof "证明"

    根据泊松过程的增量平稳性，有

    $$
    P(N(s + t) - N(s) = n) = P(N(t) = n)
    $$

    1. $n = 0$时，有$\{N(h + t) = 0, h > 0\} = \{N(h+ t) - N(t) = 0, N(t) = 0, h > 0\}$，根据增量独立性，有

        $$
        \begin{aligned}
            P(N(h + t) = 0) &= P(N(h + t) - N(t) = 0) P(N(t) = 0) \\
            &= P(N(h) = 0) P(N(t) = 0)
        \end{aligned}
        $$

        根据泊松过程的性质$P(N(t + \Delta t) - N(t) = 1) = \lambda \Delta t + o(\Delta t)$，有：

        $$
        \begin{aligned}
            \lim_{h\rightarrow 0} \frac{P(t + h) - P(t)}{h} &= \lim_{h\rightarrow 0} \frac{P(t)(1 - \lambda h - o(h)) - P(t)}{h} \\
            &= -\lambda P(t) - \lim_{h\rightarrow 0} \frac{o(h)}{h} \\
            &= -\lambda P(t)
        \end{aligned}
        $$

        解微分方程$P_0'(t) = -\lambda P_0(t)$，解得$P_0(t) = e^{-\lambda t + C}$，又因为$N(0) = 0, P_0(N(0) = 0) = 1$，得$C = 0$，从而有

        $$
        P_0(t) = e^{-\lambda t}
        $$

    2. $n > 0$时，$\{N(t + h) = n\} = \bigcup_{k = 0} ^ n \{N(t) = k, N(t + h) - N(t) = (n - k)\}$，而$n - k \geq 2$时，有$P(N(t + h) - N(t) = n - k) = o(h)$，由增量独立性

        $$
        \begin{aligned}
            P(N(t + h) = n) &= \sum_{k = 0} ^ n P(N(t) = k) P(N(t + h) - N(t) = n - k) \\
            &= P(N(t) = n)(1 - \lambda t - o(h)) + P(N(t) = n - 1)(\lambda t + o(h)) \\
            &+ \sum_{k = 2}^n P(N(t) = n - k)o(h)
        \end{aligned}
        $$

        由此

        $$
        \begin{aligned}
            &\lim_{h\rightarrow 0} \frac{P(N(t + h) = n) - P(N(t) = n)}{h} \\
            =& \lim_{h\rightarrow 0}\frac{P(N(t) = n)(\sum_{k = 2}^n P(N(t) = n - k)o(h) - P(N(t) = n)}{h} \\
            +& \lim_{h\rightarrow 0}\frac{\sum_{k = 2}^n P(N(t) = n - k)o(h) - P(N(t) = n)}{h} \\
            =& \lim_{h\rightarrow 0}\frac{P(N(t) = n)(- \lambda t) + P(N(t) = n - 1)(\lambda t)}{h} \\
        \end{aligned}
        $$

        得到

        $$
        P_n'(t) = -\lambda P_n(t) + \lambda P_{n-1}(t)
        $$

        考虑约束条件$P_n(0) = 0$，解得

        $$
        \frac{\mathrm d}{\mathrm dt}[e^{\lambda t} P_n(t)] = \lambda e^{\lambda t}P_{n - 1}(t)
        $$

        1. $n = 0$时，有$P_n(t) = e^{-\lambda t} = \frac{(\lambda t)^0}{0!}e^{-\lambda t}$
        2. 设对于$n < k$时命题成立，只需证明$n = k$时命题成立即可，有

            $$
            \begin{aligned}
                P_k(t) &= e^{-\lambda t}\int \frac{\mathrm d}{\mathrm dt}[e^{\lambda t} P_k(t)] \mathrm dt \\
                &= e^{-\lambda t}\int \lambda e^{\lambda t}P_{k - 1}(t) \mathrm dt \\
                &= e^{-\lambda t}\int \lambda \frac{(\lambda t)^{k-1}}{(k-1)!} \mathrm dt \\
                &= \frac{(\lambda t)^k}{k!}e^{-\lambda t}
            \end{aligned}
            $$

## 相邻事件时间间隔的概率分布

设$\{N(t), t \geq 0\}$为计数过程，设$S_n$表示第$n$个时间发生的时刻，即$S_n = \inf\{t, t > S_{n - 1}, N(t) = n\}$，特别地，令$S_0 = 0$。$S_n, N(t)$的事件满足

$$
\begin{aligned}
    \{S_n \leq t\} &\equiv \{N(t) \geq n\} \\
    \{N(t) = n\} &\equiv \{S_n\leq t < S_{n + 1}\} \equiv \{S_n\leq t\} - \{S_{n+1}\leq t\}
\end{aligned}
$$

由于$\{S_n \leq t\} \equiv \{N(t) \geq n\}$，可以计算$S_n$的分布函数

$$
P(S_n\leq t) = P(N(t)\geq n) = 1 - e^{-\lambda t}\sum_{k=0}^{n-1} \frac{(\lambda t)^{k}}{k!}
$$

特别地，当$n = 1$时，有$P(X_1\leq t) = P(S_1\leq t) = (1 - e^{-\lambda t}) I_{\{t\geq 0\}}$

计数过程$\{N(t), t\geq 0\}$是泊松过程的充要条件是$\{X_n = S_{n} - S_{n-1}, n\geq 1\}$独立同分布，服从的分布为参数$\lambda$的指数分布。

???+ proof "证明"

    1. $\Leftarrow$：必要性证明，先求$S_1, \cdots, S_n$的联合概率密度函数，设$t_1 < t_2 < \cdots < t_n$，设$h$为充分小的正数，满足

        $$
        t_1 + \frac h2 < t_2 - \frac h2 < t_2 + \frac h2 < \cdots < t_n - \frac h2
        $$

        考虑如下事件

        $$
        \begin{aligned}
            &\left\{t_1 - \frac h2 < S_1 \leq t_1 + \frac h2, t_2 - \frac h2 < S_2 \leq t_2 + \frac h2, \cdots, t_n - \frac h2 < S_n \leq t_n + \frac h2\right\}
            &\equiv \left\{N\left(t_1 - \frac h2\right) = 0, N\left(t_1 + \frac h2\right) - N\left(t_1 - \frac h2\right) = 1, N\left(t_2 - \frac h2\right) - N\left(t_1 + \frac h2\right) = 0, \cdots, N\left(t_n + \frac h2\right) - N\left(t_n - \frac h2\right) \geq 1\right}
        \end{aligned}
        $$
    2. $\Rightarrow$：充分性证明，设$\{X_k, k\geq 1\}$独立同指数分布，设$S_0 = 0, S_n = S_0 + \sum_{i = 1}^n X_i$。定义

        $$
        N(t) = \sum_{n=1}^\infty I_{\{S_n\leq t\}}
        $$

        * 由于$I_{\{S_n\leq t\}}\in \mathbb N$，则$N(t)\in \mathbb N$。
        * 对于$t > s$，有

            $$
            N(t) - N(s) = \sum_{n = 1}^\infty I_{\{S_n\leq t\}}- I_{\{S_n\leq s\}}
            $$

            而$S_n - S_{n-1} = X_n > 0$，因此$S_n$为单调增序列，从而$\{S_n\leq s\}\subset \{S_n\leq t\}$，即$I_{\{S_n\leq t\}}- I_{\{S_n\leq s\}} \geq 0$，因此$N(t) - N(s)$

        可得$N(t)$为计数过程。以下证明$N(t)$为泊松过程：