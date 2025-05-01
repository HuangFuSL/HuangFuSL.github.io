# 动态规划方法

对于简单的强化学习环境，如果环境的状态转移完全可知，则可以使用动态规划方法对问题进行求解。

## 概念定义

???+ definition "价值函数"

    状态-价值映射又称为价值函数$V_\pi(s)$，指智能体按照策略$\pi$执行，处于状态$s$时所能获得的期望回报。

    $$
    V_\pi(s) \triangleq \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t r_t \middle | s_0 = s \right]
    $$

???+ definition "Q函数"

    Q函数是动作-价值映射$Q_\pi (s, a)$，指智能体从状态$s$采取动作$a$开始，之后按照策略$\pi$执行，所能得到的期望回报。

    $$
    Q_\pi(s, a) \triangleq \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t r_t \middle | s_0 = s, a_0 = a \right]
    $$

???+ definition "提升函数"

    提升函数是智能体在当前状态采取动作$a$，相较于严格按照策略$\pi$执行所能获得的期望回报的提升。

    $$
    A_\pi (s, a) \triangleq Q_\pi(s, a) - V_\pi(s)
    $$

    提升函数满足

    $$
    E_{\pi(s\mid a)} \left[ A_\pi (s, a) \right] = 0
    $$

最优策略是能够最大化所有状态的价值函数的策略，即$V^*(s) \geq V_\pi(s), \forall \pi$。状态-价值映射和动作-价值映射最优，当且仅当满足Bellman最优性或Bellman方程：

$$
\begin{aligned}
V^*(s) &= \max_{a} \left[R(s, a) + \gamma \sum_{s'} P(s'|s, a)V^*(s')\right] \\
Q^*(s, a) &= R(s, a) + \gamma \sum_{s'} P(s'|s, a)V^*(s')
\end{aligned}
$$

Bellman方程可以写成向量形式：

$$
\begin{aligned}
& \bsv = \bsr_{\pi} + \gamma \bsP_{\pi} \bsv \\
\text{where} & \left\{\begin{aligned}
\bsv_s &= V^*(s) \\
\bsr_{\pi, s} &= \sum_a \pi(a|s) R(s, a) \\
\bsP_{\pi, s, s'} &= \sum_a \pi(a|s) P(s'|s, a)
\end{aligned}\right.
\end{aligned}
$$

最优策略可以通过动作-价值函数导出。

$$
\pi^*(s) = \arg \max_a Q^*(s, a)
$$

更新策略的过程称为策略优化，根据策略计算状态价值函数和动作价值函数的过程称为策略评估。

## 价值迭代

价值迭代是动态规划方法中最简单的一种。它的基本思想是通过迭代更新状态价值函数，直到收敛为止。价值迭代的步骤如下：

$$
V_{s + 1}(s) = \max_{a} \left[R(s, a) + \gamma \sum_{s'} P(s'|s, a)V_s(s')\right]
$$

计算贝尔曼残差$\Delta_k = \max_s |V^*(s) - V_k(s)|$，满足

$$
\begin{aligned}
\Delta_k &= \max_s [V^*(s) - V_k(s)] \\
\Delta_{k + 1} &= \max_s [V^*(s) - V_{k + 1}(s)] \\
&= \max_s \left[\max_{a} \left[R(s, a) + \gamma \sum_{s'} P(s'|s, a)V^*(s')\right] - \max_{a} \left[R(s, a) + \gamma \sum_{s'} P(s'|s, a)V_k(s')\right]\right] \\
&\leq \max_s \left[ \max_a \gamma \sum_{s'} P(s'|s, a)(V^*(s') - V_k(s')) \right] \\
&=\max_s \left[V^*(s) - V_k(s)\right] \\
&\leq \gamma \Delta_k
\end{aligned}
$$

因此，价值迭代算法能保证对价值函数的估计逐渐趋近最优。价值迭代无论是同时更新所有状态的价值函数，还是逐个更新状态的价值函数，都是收敛的。

## 策略迭代

策略迭代是一种常用的求解动态规划问题的方法。它包含两个步骤，即策略评估和策略提升。在策略评估阶段，算法根据当前策略和上一次迭代的状态价值函数，计算当前的状态价值函数。

$$
\bsv_{k + 1} = \bsr_{\pi_k} + \gamma \bsP_{\pi_k} \bsv_k
$$

在策略提升阶段，算法根据当前的状态价值函数，计算出一个新的策略。

$$
\pi_{k + 1}(s) = \arg \max_a \left[R(s, a) + \gamma \sum_{s'} P(s'|s, a)V_k(s')\right]
$$

可以证明，$\bsv_{k + 1}\geq \bsv_k$。
