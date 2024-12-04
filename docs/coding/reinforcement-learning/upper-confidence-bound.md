# 置信上界算法

置信上界（Upper Confidence Bound, UCB）算法的核心思想是将尝试次数纳入考虑，尝试次数较少的动作有更大的不确定性，算法会尽可能乐观地考虑这些没有尝试过的动作，并优先探索这些动作。在每个动作探索比较深入后，再转向利用奖励较高的动作。

!!! note "引理"

    设随机变量$X_1, \ldots, X_n$独立同分布，均值为$0$，对均值的估计为

    $$
    \hat \mu = \frac{1}{n}\sum_{i=1}^n X_i
    $$

    则对任意$\delta > 0$，有

    $$
    P(\hat\mu > \delta) \leq \exp(-n\delta^2 / 2)
    $$

    该引理称为[Hoeffding不等式](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality)。

    令$\varepsilon = \exp(-2n\delta^2)$，即$\delta = \sqrt{\frac{-2\log\varepsilon}{n}}$

    $$
    P\left(\hat\mu > \sqrt{\frac{-2\log\varepsilon}{n}}\right) \leq \varepsilon
    $$

对于每个动作$k$，我们尝试了$n_k$次，每次尝试的奖励为$X_1, \ldots, X_{n_k}$，观测到的平均奖励为$\hat\mu_k$，定义$\tilde X_i = X_i - \hat\mu_k$，则$\tilde X_1, \ldots, \tilde X_{n_k}$独立同分布，均值为$0$。

令对$\tilde X_1, \ldots, \tilde X_{n_k}$估计的均值为$\hat\mu_0$，我们有$1 - \varepsilon$的概率保证$\hat\mu_0$不超过$\sqrt{\frac{-2\log\varepsilon}{n_k}}$。

$$
P\left(\hat\mu_0 > \sqrt{\frac{-2\log\varepsilon}{n_k}}\right) \leq \varepsilon
$$

因此，我们取$\hat\mu_k + \sqrt{\frac{-2\log\varepsilon}{n_k}}$作为动作$k$的置信上界。通过调整$\varepsilon$，我们可以控制置信上界的宽度以在探索和利用之前取得平衡。

通常采取的策略是取$\varepsilon = 1/t$，$t$为总轮次，以保证随着尝试次数的增加，置信上界的宽度逐渐减小，使得算法逐步转向利用，此时有

$$
\hat\mu_k + \sqrt{\frac{2\log t}{n_k}}
$$

此外，也可以使用其他的上界宽度，如

$$
\varepsilon = \frac{1}{1 + t\log^2 t}
$$

在实践中，通常还会引入一个参数$c$控制宽度，即

$$
\hat \mu_k + c\cdot\sqrt{\frac{\log t}{n_k}}
$$
