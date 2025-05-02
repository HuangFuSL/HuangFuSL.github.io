# 时序差分学习

在更为复杂的强化学习环境中，我们往往无法获知环境的状态转移概率分布，无法计算Bellman方程中的$\sum_{s'} P(s'|s, a)V^*(s')$部分。导致不能使用动态规划的方法来求解最优策略。时序差分学习是一种基于采样的方法来估计价值函数的方法。

## 蒙特卡洛估计

蒙特卡洛方法是一种基于采样的方法。给定策略$\pi$，我们可以通过反复执行该策略，直到价值函数估计收敛或到达吸收状态。即，对环境进行多次采样来估计状态的价值函数。

$$
V(s_t) = V(s_t) + \eta \left[G_t - V(s_t)\right]
$$

相同地，我们也可以估计动作价值函数$Q(s_t, a_t)$。在获得对动作价值函数的估计后，可以使用策略迭代的方式更新策略。

## 时序差分学习

通过蒙特卡洛估计的方法学习$V(s_t)$和$Q(s_t, a_t)$的缺点在于其估计的方差较大，并且，其需要等到估计收敛或到达吸收状态后才能更新价值函数，采样时间较长。时序差分学习（Temporal Difference Learning）利用仅采样一步得到的奖励，结合价值函数来估计价值函数估计的偏差。

$$
\begin{aligned}
V(s_t) &= V(s_t) + \eta \left[r_t + \gamma V(s_{t + 1}) - V(s_t)\right] \\
Q(s_t, a_t) &= Q(s_t, a_t) + \eta \left[r_t + \gamma Q(s_{t + 1}, a') - Q(s_t, a_t)\right]
\end{aligned}
$$

其中$r_t + \gamma V(s_{t + 1})$和$r_t + \gamma Q(s_{t + 1}, a')$称为TD target，$V(s_t)$和$Q(s_t, a_t)$应当向TD target收敛。两者之差称为TD error。

若函数$V(s_t)$的参数为$\theta$，则时序差分学习的更新公式可以表示为：

$$
\theta \leftarrow \theta + \eta \left[r_t + \gamma V_\theta(s_{t + 1}) - V_\theta(s_t)\right] \nabla_\theta V_\theta(s_t)
$$

$Q(s_t, a_t)$的更新公式同理。

对于一个状态转移过程$(s_t, a_t, r_t, s_{t + 1})$和，根据动作$a'$的选择方式，我们可以将时序差分学习分为两种类型：on-policy和off-policy。

* **on-policy**：SARSA是一种on-policy的时序差分学习方法，动作$a'$根据当前策略（如$\epsilon$-greedy等）选择
* **off-policy**：Q-learning是一种off-policy的时序差分学习方法，动作$a'$可以任意选择，如贪心选择等。

## TD与MC的比较

定义$n$步回报$G_{t:t + n}$为：

$$
G_{t:t + n} = \sum_{k = 0}^{n - 1} \left(\gamma^k r_{t + k}\right) + \gamma^n V(s_{t + n})
$$

TD学习只看下一步的回报$G_{t:t + 1}$，而MC学习则是看$\infty$步的回报$G_{t:t + \infty}$。定义$\lambda$为平衡短期回报和长期回报的参数，$0 \leq \lambda \leq 1$，通过指数衰减的方式来平衡短期回报和长期回报：

$$
G_t^\lambda = \sum_{n = 1}^{\infty} \lambda^{n - 1} G_{t:t + n}
$$

使用该$G_t^\lambda$来更新价值函数的方式称为TD($\lambda$)方法。

* TD学习等价于$\lambda = 0$
* MC学习等价于$\lambda = 1$
