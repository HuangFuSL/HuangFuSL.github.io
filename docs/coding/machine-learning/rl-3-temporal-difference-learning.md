# 时序差分学习

在更为复杂的强化学习环境中，我们往往无法获知环境的状态转移概率分布，无法计算Bellman方程中的$\sum_{s'} P(s'|s, a)V^*(s')$部分。导致不能使用动态规划的方法来求解最优策略。此时我们只能通过与环境交互，获取奖励，以此来估计状态价值函数$V(s)$和动作价值函数$Q(s, a)$。在强化学习中，最常用的两种方法是蒙特卡洛方法（Monte Carlo Method）和时序差分学习（Temporal Difference Learning）。

**交互**指智能体从当前状态$s_t$出发，按照某个策略$\pi(a\mid s)$选择一个动作$a_t$，并与环境交互，获得下一个状态$s_{t + 1}$和奖励$r_t$。

* 蒙特卡洛方法：从状态$s_0$出发，按照某个策略不断与环境交互，直到到达终止状态，以此来估计状态价值函数和动作价值函数。
* 时序差分学习：智能体与环境做一步交互，结合当前对状态价值函数的估计，来更新状态价值函数和动作价值函数。

根据用于选择动作策略的来源，我们可以将时序差分学习分为两种类型：on-policy和off-policy。

* on-policy：$a_t$必须是在状态$s_t$下，按照当前策略$\pi(a\mid s)$选择的动作。
* off-policy：$a_t$可以是来自任何策略选择的动作。

## 蒙特卡洛估计

蒙特卡洛方法是一种基于采样的方法。给定策略$\pi$，我们可以通过反复执行该策略，直到价值函数估计收敛或到达吸收状态。即，对环境进行多次采样来估计当前策略下状态的价值。

$$
\hat V_\pi(s_0) = \sum_{t = 0}^{T} \gamma^t R(s_t, \pi(s_t)) \leftarrow \sum_{t = 0}^{T} \gamma^t r_t
$$

相同地，我们也可以估计动作价值函数$Q(s_t, a_t)$

$$
\hat Q_\pi(s_0, a_0) = R(s_0, a_0) + \sum_{t = 1}^{T} \gamma^t R(s_t, \pi(s_t)) \leftarrow \sum_{t = 0}^{T} \gamma^t r_t
$$

在获得对动作价值函数的估计后，可以使用策略迭代的方式更新策略。

## 时序差分学习

通过蒙特卡洛估计的方法学习$V(s_t)$和$Q(s_t, a_t)$的缺点在于其估计的方差较大，并且，其需要等到估计收敛或到达吸收状态后才能更新价值函数，采样时间较长。时序差分学习（Temporal Difference Learning）利用仅采样一步得到的奖励，估算价值函数。

$$
\begin{aligned}
\hat V(s_t) &= R(s_t, \pi(s_t)) + \gamma V_\pi(s_{t + 1}) \leftarrow r_t + \gamma V_\pi(s_{t + 1})  \\
\hat Q(s_t, a_t) &= R(s_t, a_t) + \gamma Q_\pi(s_{t + 1}, a')\leftarrow r_t + \gamma Q_\pi(s_{t + 1}, a')
\end{aligned}
$$

称为TD Target。优化目标为价值函数向TD Target的最小化均方误差，即

$$
\calL(\pi) = (\hat V(s_t) - V_\pi(s_t))^2 = (\hat Q(s_t, a_t) - Q_\pi(s_t, a_t))^2
$$

若函数$V(s_t)$的参数为$\theta$，则时序差分学习的更新公式可以表示为：

$$
\theta \leftarrow \theta + \eta \left[r_t + \gamma V_\theta(s_{t + 1}) - V_\theta(s_t)\right] \nabla_\theta V_\theta(s_t)
$$

$Q(s_t, a_t)$的更新公式同理。

* SARSA：on-policy的时序差分学习方法，使用当前策略$\pi(a\mid s)$来选择动作$a_t, a'$。
* Q-learning：off-policy的时序差分学习方法，通常用贪心策略来选择动作$a'$，$a_t$可以是任何策略选择的动作。

## TD与MC的比较

由于TD涉及用当前的价值函数来估计下一步的价值函数，若当前的价值函数有偏，则会将偏差引入到下一步的价值函数中。因此，TD方法可以减小估计的方差，但会引入偏差。相反，MC方法是无偏的，但方差较大。

定义$n$步回报$G_{t:t + n}$为：

$$
G_{t:t + n} = \sum_{k = 0}^{n - 1} \left(\gamma^k r_{t + k}\right) + \gamma^n V(s_{t + n})
$$

TD学习只看下一步的回报$G_{t:t + 1}$，而MC学习则是看$\infty$步的回报$G_{t:t + \infty}$。定义$\lambda$为平衡短期回报和长期回报的参数，$0 \leq \lambda \leq 1$，通过指数衰减的方式控制短期回报和长期回报的权重，从而平衡偏差和方差。

$$
G_t^\lambda = \sum_{n = 1}^{\infty} \lambda^{n - 1} G_{t:t + n}
$$

使用该$G_t^\lambda$来更新价值函数的方式称为TD($\lambda$)方法。

* TD学习等价于$\lambda = 0$
* MC学习等价于$\lambda = 1$
