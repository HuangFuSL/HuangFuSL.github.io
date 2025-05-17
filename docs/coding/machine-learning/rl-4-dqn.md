# 深度Q网络

如果环境的状态空间和动作空间较大，或者是连续的，此时就不再能使用表格的方式来存储动作价值函数$Q(s, a)$了。此时可以使用函数近似的方法，用一个参数化的函数$Q(s, a; \theta)$来近似动作价值函数$Q(s, a)$。其中$\theta$为函数的参数。在离散情况下，$Q$函数的更新方式为

$$
Q(s_t, a_t) = Q(s_t, a_t) + \eta \left[r_t + \gamma \max_{a'} Q(s_{t + 1}, a') - Q(s_t, a_t)\right]
$$

若用函数近似，则可以用

$$
\calL = \left[\underbrace{r_t + \gamma \max_{a'} Q(s_{t + 1}, a'; \theta)}_{\text{TD target}} - Q(s_t, a_t; \theta)\right]^2
$$

作为优化目标以实现更新。为了提高样本的利用率，可以使用经验回放的方式存储$(s_t, a_t, r_t, s_{t + 1})$，以供后续的训练。

基于函数近似的Q-Learning存在一个“致命三要素”，会导致训练过程的不稳定，甚至发散：

* TD estimation本身存在偏差的问题。
1. 使用函数近似的方式来估计动作价值函数$Q(s, a)$。函数近似的方式会存在估计偏差。
2. 使用bootstrap的方式来生成训练样本，存在放大估计偏差的风险。
3. 训练过程的策略是off-policy的，导致目标策略和行为策略不匹配。

在训练过程中，Q Loss往往会在一个值范围内震荡，但不影响reward的提升。为了缓解“致命三要素”的问题，可以使用以下方法改进DQN：

* 目标网络：使用两个网络$Q_\theta$和$Q_{\theta'}$，其中$Q_{\theta'}$为目标网络，$Q_\theta$为当前网络。当前网络用于计算动作价值函数，而目标网络用于计算TD target，其更新滞后于当前网络。有两种更新方式：
  * 每隔一段时间更新一次目标网络的参数$\theta' \leftarrow \theta$。
  * 使用指数平滑的方式更新目标网络的参数$\theta' \leftarrow \tau \theta + (1 - \tau) \theta'$，其中$\tau$为平滑系数。
  * 双时间尺度：在训练过程中为目标网络和当前网络设置不同的学习率。
* 多步采样：在采样环境反馈时，多向前采样若干步。$(s_0, a_0, r_0, s_1, a_1, r_1, \ldots, s_n, a_n, r_n, s_{n + 1})$，$Q$函数的更新目标变为：

  $$
  \text{TD\,target} = \sum_{i = 0}^n \gamma^i r_i + \gamma^{n + 1} \max_{a'} Q(s_{n + 1}, a'; \theta)
  $$

* 优先经验回放：在计算过样本的TD Loss后，存储该TD Loss。在后续的训练中优先选择TD Loss较大的样本进行训练。
* 分布式DQN：在计算TD Loss时，使用分布式的方式来计算TD Loss。即将TD Loss视为一个分布，而不是一个值。可以使用分布式的方式来计算TD Loss的均值和方差，从而提高训练的稳定性。
* 噪声网络：在Q函数中引入一个噪声输入。训练初期噪声对Q函数的影响较大，表现为探索性较强。随着训练的进行，模型逐渐消除噪声的影响，表现为利用性较强。
* 使用Double DQN和Dueling DQN等DQN变种。

[Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298)对比了运用以上训练技巧的DQN变种的性能。

## Double DQN

DQN存在Q函数被系统性高估的风险。Double Q-Learning使用两个函数$Q_1$和$Q_2$，按照如下过程更新参数：

$$
Q_1(s_t, a_t) = Q_1(s_t, a_t) + \eta \left[r_t + \gamma Q_1(s_{t + 1}, \arg\max_{a'} Q_2(s_{t + 1}, a'); \theta) - Q_1(s_t, a_t)\right]
$$

即对于$Q_1$，使用$Q_2$选择动作、$Q_1$计算TD Loss，反之亦然。

不同的是，Double DQN对于$Q_1$，使用$Q_1$选择动作、$Q_2$计算TD Loss。

## Dueling DQN

Dueling DQN将$Q(s, a)$分解为两个函数$V(s)$和$A(s, a)$，即当前策略下的状态价值函数和优势函数。对于最优策略，满足$\max_{a'} A(s, a') = 0$

$$
Q(s, a) = V(s) + A(s, a) - \max_{a'} A(s, a')
$$

代替DQN中的Q函数即可。在实现中通常使用均值代替最大值，网络更容易收敛。
