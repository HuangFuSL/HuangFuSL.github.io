# 策略梯度方法

基于Q学习的DQN面临如下问题：

* 仅适合处理离散动作空间的问题，由于计算过程中需要在$\mathcal{A}$上计算$\max$，在无限动作空间上无法实现。
* 使用函数近似的方法会导致估计的Q值存在偏差，策略可能不稳定甚至发散。
* Q值的优化和最终收益的优化之间存在不一致，并不能保证Q值的优化会导致最终收益的优化。
* Q学习仅能学习到确定性的策略，而不是学习到策略的分布。

相比之下，策略模型则直接学习到动作的分布$\pi(a\mid s; \theta)$。策略模型的优化目标为最大化收益

$$
\begin{aligned}
J(\theta) &= \mathbb{E}_{\pi_\theta} \sum_{t=0}^\infty \gamma^t r_{t + 1} \\
&= \sum_{t = 0}^\infty \gamma^t \sum_{s_t} P(s_t) \sum_{a_t} \pi(a_t\mid s_t; \theta) R(s_t, a_t) \\
&= \sum_{t = 0}^\infty \gamma^t \sum_{s_t} \sum_{s_0} P(s_0) P(s_t\mid s_0, \pi) \sum_{a_t} \pi(a_t\mid s_t; \theta) R(s_t, a_t) \\
&= \sum_{t = 0}^\infty \sum_{s}\sum_{s_0} \gamma^t P(s_0) P(s_t = s\mid s_0, \pi) \sum_{a} \pi(a\mid s; \theta) R(s, a) \\
&= \sum_{s}\sum_{s_0} \sum_{t = 0}^\infty \gamma^t P(s_0) P(s_t = s\mid s_0, \pi) \sum_{a} \pi(a\mid s; \theta) R(s, a) \\
\end{aligned}
$$

定义$\rho_\gamma^\pi (s) = \sum_{s_0} \sum_{t = 0}^\infty \gamma^t P(s_0) P(s_t = s\mid s_0, \pi)$为策略$\pi$下，状态$s$按$\gamma$折扣后的概率分布。

$$
J(\theta) = \sum_{s} \rho_\gamma^\pi (s) \sum_{a} \pi(a\mid s; \theta) R(s, a)
$$

即

$$
J(\theta) = \mathbb{E}_{s\sim \rho_\gamma^\pi, a\sim \pi(a\mid s; \theta)} \left[ R(s, a) \right]
$$

计算$J$对$\theta$的梯度，近似假设$\nabla_\theta\rho_\gamma^\pi (s) = 0$。注意到$\nabla_\theta \pi(a\mid s; \theta) = \pi(a\mid s; \theta) \nabla_\theta \log \pi(a\mid s; \theta)$。由于改变动作$a$会导致后续的所有路径发生变化，使用$Q^{\pi_\theta}(s, a)$替换$R(s, a)$，表示从动作$a$后当前策略策略$\pi_\theta$的长期回报，类似地，我们同样忽略$Q$对$\theta$的梯度。

$$
\begin{aligned}
\nabla_\theta J(\theta) &= \sum_{s} \rho_\gamma^\pi (s) \sum_{a} \nabla_\theta \pi(a\mid s; \theta) Q^{\pi}(s, a) \\
&= \sum_{s} \rho_\gamma^\pi (s) \sum_{a} \pi(a\mid s; \theta) Q^{\pi_\theta}(s, a) \nabla_\theta \log \pi(a\mid s; \theta) \\
&= \mathbb E_{s\sim \rho_\gamma^\pi, a\sim \pi(a\mid s; \theta)} \left[ Q^{\pi_\theta}(s, a) \nabla_\theta \log \pi(a\mid s; \theta) \right] \\
\end{aligned}
$$

称为**策略梯度定理**。$\nabla_\theta \log \pi(a\mid s; \theta)$称为**得分函数**。直观理解，策略梯度定理指明了策略函数优化的方向是对未来回报提升最快的参数方向，最大化有价值的行为发生的概率

## REINFORCE

REINFORCE使用蒙特卡洛方法估计Q值。假设对于一个路径$\{s_0, a_0, r_0, s_1, a_1, r_1, \ldots s_T\}$。REINFORCE使用$G_t \triangleq \sum_{k = 0}^{T - t - 1} \gamma^k r_{t + k}$作为对$Q^{\pi_\theta}(s_t, a_t)$的估计。随后按照策略梯度定理更新梯度。
