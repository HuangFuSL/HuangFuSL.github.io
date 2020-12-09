# 常见排队模型

一个排队模型主要由以下部分组成

* 顾客（实体）处理
* 实体排队等待处理（系统的排队策略可能不同，损失制不允许排队、混合制允许排有限长度的队列）
* 实体处理完毕，离开系统

## 排队模型的描述

### 进入系统

假设进入系统的实体数量无限。考察相邻两个实体进入系统的时间差：

1. 对于定长分布，实体进入系统的时间差为常量$t$，$t$概率密度函数为：

$$
f(t; \alpha)=\left\{
\begin{aligned}
    & 1 & t=\alpha \\
    & 0 & t\not =\alpha
\end{aligned}
\right .
$$

2.  Poisson 流，实体进入系统的时间差独立同分布，服从参数为$\lambda$的指数分布

$$
f_{\xi_i}(t; \lambda)=\left\{
\begin{aligned}
    & \lambda e^{-\lambda t} & t\geq 0 \\
    & 0 & t < 0
\end{aligned}
\right .
$$

3. Erlang 分布，实体进入系统的时间差独立同分布，服从如下公式所示的分布。若某个系统中有$K$个并联的服务台，输入实体为 Poisson 流，则第$K$个服务台的顾客流为 Erlang 流，前面所有$K - 1$个服务台在第一个实体到达以后的输入流同样为 Erlang 流。

$$
f(t; \lambda, K)=\left\{
\begin{aligned}
    & \frac{\lambda(\lambda t)^{K-1}}{(K-1)!} & t\geq 0 \\
    & 0 & t < 0
\end{aligned}
\right .
$$

### 实体排队与处理

系统中可能有一个或多个服务台。在系统中的所有服务台都处于运行状态时，新进入的实体无法立即进行处理，而是进入队列或直接离开，取决于系统的排队策略。排队策略可以分为损失制、等待制与混合制。  

在损失制系统中，如果新进入的实体不能被立即处理，则会离开系统。  
在等待制系统中，如果新进入的实体不能被立即处理，则会在队列中等待，直到被处理。  
在混合制系统中，如果新进入的实体不能被立即处理且此时的队列长度大于某一常数值，则会离开系统，否则会进入队列等待。

实体在排队过程中的行为可以分为如下类型：

* 离开：当实体得知需要等待或没有耐心继续等待时，实体可能退出队列
* 变换：即实体为减少排队时间而在不同服务台的队列之间移动

服务台会按照如下可能的方式进行服务：

* FCFS：先进入队列的先进行处理
* LCFS：后进入队列的先进行处理
* 随机处理
* PS：优先级高的实体先进行处理
* 断续处理：在处理某个实体一段时间后，转而处理另一个实体，不断循环直到实体处理完成

在系统中的服务台的服务时间是一个随机变量，概率分布为常数、指数分布、K级 Erlang 分布、一般分布等。

### 系统的符号表示

Kendall记号，格式为$X/Y/Z/A/B/C$

* $X$表示实体到达间隔时间的分布
  * $M$表示到达过程为 Poisson 过程（间隔时间服从指数分布）或负指数分布
  * $D$表示间隔时间为常数
  * $E_k$表示间隔时间服从$k$阶 Erlang 分布
  * $G$表示间隔时间服从一般、相互独立的随机分布
* $Y$表示服务台单次服务时间的分布，记号与$X$的含义相同
* $Z$表示服务台个数
* $A$表示系统的等待空间容量，$0$为损失制系统，$\infty$为等待制系统，否则为混合制系统。
* $B$表示实体的总数量，$\infty$表示实体源无限
* $C$表示服务规则

$A, B, C$参数可以省略。分别等价于$\infty, \infty, \mathit{FCFS}$

### 系统的观测指标

衡量系统性能的常用观测指标为：

* $N(L)$：稳态系统的队长（指系统内所有的实体数量）
* $N_q(L_q)$稳态系统的排队长
* $T(W)$：顾客在稳态系统中的停留时间（处理+等待）
* $T_q(W_q)$：顾客在稳态系统中的等待时间
* $p_n$：稳态系统任意时刻状态为$n$的概率，$p_n=P(N=n)=\lim_{t\rightarrow \infty}P(N(t) = n)$
* $\rho$：利用率
* $p_D$：实体进入系统时需要等待的概率

若将系统视为管道，系统中实体的数量等于实体进入系统的速度与系统平均响应（处理）时间之积。

对于$M/M/s$系统，令$\lambda$为实体进入系统的速度，$\mu$为服务台处理实体的速度，$s$为服务台的数量，则：

$$
\begin{aligned}
L &= \lambda_e W \\
L_q &= \lambda_e W_q
\end{aligned}
$$

## 随机过程

常见的随机过程有 Markov 过程、生灭过程、 Poisson 过程等。所有的 Poisson 过程都是生灭过程，所有的生灭过程都是 Markov 过程。

### Markov 过程

特点：**$t_0$时刻的状态与任意$t<t_0$时的状态无关**

Markov 链由马尔可夫过程中的离散状态组合。对于 Markov 过程，系统无记忆性，当前的状态不会对后面的状态产生影响。

$M/M/s$系统可以使用 Markov 过程建模。队列中实体的数量是一个 Markov 链。

### 生灭过程

生灭过程按如下图进行描述（状态转移图）：

![Birt-Death Process](img/12-1.svg)

假设实体离散进入的$M/M/s$系统，队列中的实体数量服从生灭过程

### Poisson 过程

实体进入的时间差相互独立且服从同一指数分布的过程

## 生灭过程

对于生灭过程，有如下假设

* 每个时刻只有一个实体进入系统
* 定义系统的状态为系统中的实体数量$n$
  * 一个实体进入系统，系统的状态由$n-1$转变为$n$
  * 一个实体离开系统，系统的状态由$n$转变为$n+1$
* 系统处于状态$n$时，定义实体进入的速度为$\lambda _n$，系统的处理速度为$\mu_n$。对于$\lambda_n$，$n\geq 0$；对于$\mu_n$，$n>0$

问题：系统处于稳定状态时，生灭系统处于状态$n$的概率$p_n$？

对于处于状态$j$的系统，考察一个极短的时间间隔$\Delta t$，由于$\Delta t$极短，可以忽略$\Delta t$时间内两个实体同时进入/离开系统或一个实体进入、一个实体离开系统的情况。$\Delta t$时间内系统发生变化的概率如下：

* 一个实体进入系统：$P(n(t+\Delta t)=j+1 | n(t) = j)=\lambda_j\Delta t$
* 一个实体离开系统：$P(n(t+\Delta t)=j-1| n(t) = j) = \mu_j\Delta t$
* 系统在$\Delta t$时间内没有发生状态改变：$P(n(t+\Delta t) = j | n(t)=j) = 1 - (\lambda_j+\mu_j)\Delta t$

根据假设，处于状态$i$的系统在$t+\Delta t$时只可能处于$i-1, i, i+1$三种状态中的一种。也即，处于状态$i$的系统在$t-\Delta t$时只可能处于$i-1, i, i+1$三种状态中的一种。由此，可以列式如下：

$$
\begin{aligned}
  p_0(t+\Delta t) &= (1-\lambda_0\Delta t)p_0(t) + \mu_1\Delta tp_1(t) \\
  p_j(t+\Delta t) &= \lambda_{j-1}\Delta tp_{j-1}(t)+(1-\mu_j\Delta t-\lambda_j\Delta t)p_j(t)+\mu_{j+1}\Delta tp_{j+1}(t)
\end{aligned}
$$

整理后取极限$\Delta t\rightarrow 0$，上式变为导数形式：

$$
\begin{aligned}
  &\lim_{\Delta t\rightarrow 0} \frac{p_j(t+\Delta t)-p_j(t)}{\Delta t}=\lambda_{j-1}p_{j-1}(t)+\mu_{j+1}p_{j+1}(t) - (\mu_j+\lambda_j)p_j(t) \\
  \Rightarrow &\frac{\mathrm dp_j(t)}{\mathrm dt}=\lambda_{j-1}p_{j-1}(t)+\mu_{j+1}p_{j+1}(t) - (\mu_j+\lambda_j)p_j(t)
\end{aligned}
$$

当$t\rightarrow \infty$时，系统趋于稳态，则有$\lim_{t\rightarrow \infty}p_j(t) = p_j$，收敛的充分必要条件为$\lim_{t\rightarrow\infty} \frac{\mathrm dp_j(t)}{\mathrm dt}=0$。即$\lambda_{j-1}p_{j-1}(t)+\mu_{j+1}p_{j+1}(t) - (\mu_j+\lambda_j)p_j(t)=0$。

解$p_{j+1}$，解得：

$$
p_{j+1} = \left(\frac{\mu_j+\lambda_j}{\mu{j+1}}\right)p_j-\frac{\lambda_{j-1}}{\mu_{j+1}}p_{j-1}
$$

对于$p_1$，有$p_1=\frac{\lambda_0}{\mu_1}p_0$。

根据递推公式，可以用$p_0$表示出$p_j$：

$$
\begin{aligned}
  p_2&=\left(\frac{\mu_1+\lambda_1}{\mu_2}\right)p_1-\frac{\lambda _0}{\mu_2}p_0 = \frac{\lambda_0(\mu_1+\lambda_1)}{\mu_1\mu_2}p_0-\frac{\lambda_0}{\mu_2}p_0=\frac{\lambda_0\lambda_1}{\mu_1\mu_2}p_0 \\
  p_3&=\left(\frac{\mu_2+\lambda_2}{\mu_3}\right)p_2-\frac{\lambda_1}{\mu_3}p_1=\frac{\lambda_0\lambda_1(\mu_2+\lambda_2)}{\mu_1\mu_2\mu_3}p_0-\frac{\lambda_0\lambda_1}{\mu_1\mu_3}p_0=\frac{\lambda_0\lambda_1\lambda_2}{\mu_1\mu_2\mu_3}p_0 \\
  &\vdots \\
  &p_j = \frac{\lambda_0\lambda_1\cdots\lambda_{j-1}}{\mu_1\mu_2\cdots\mu_j}p_0=p_0\prod_{i = 1}^{j}\frac{\lambda_{i-1}}{\mu_j}
\end{aligned}
$$

由于系统的状态只可能取$0\sim\infty$之间的整数值，概率之和为$1$，可以计算出$p_0$：

$$
p_0=\frac{1}{1+\sum_{n=1}^\infty \prod_{i=0}^{n}\frac{\lambda_{i-1}}{\mu_i}}
$$

### M/M/1队列

对于$M/M/1$系统，$\lambda_0=\lambda_1=\cdots=\lambda_n=\lambda, \mu_1=\cdots=\mu_n=\mu$。

由此，计算出$M/M/1$系统在稳态时处于$p_0$的概率：

$$
p_0=\frac{1}{1+\sum_{n=1}^\infty \prod_{i=0}^{n}\frac{\lambda}{\mu}} = \frac{1}{1+\sum_{n=1}^\infty \rho^n}=\frac{1}{\sum_{n=0}^\infty \rho^n}=1-\rho
$$

概率分布为：$P(N=n)=\rho^n(1-\rho)$

### M/M/s队列

对于$M/M/s$系统，$\lambda_i, \mu_i$服从如下规律：

* $\lambda_i = \lambda \qquad i=0, 1\cdots, \infty$
* $\mu_i = \max\{i, s\}\mu \qquad i=1, 2, \cdots, \infty$

计算出$M/M/s$系统在稳态时处于$p_0$的概率，令$\rho_0=\frac{\lambda}{\mu}$：

$$
\begin{aligned}
  p_0&=\frac{1}{1+\sum_{n=1}^\infty \prod_{i=0}^{n}\frac{\lambda}{\max\{i, s\}\mu}} \\
  &= \frac{1}{\sum_{i=0}^{s-1}\frac{\rho_0^i}{i!}+\sum_{i=s}^\infty \frac{\rho_0^i}{s!s^{i-s}}} \\
  &=\frac{1}{\sum_{i=0}^{s-1}\frac{\rho_0^i}{i!}+\frac{\rho_0^s}{s!}\sum_{i=0}^\infty \frac{\rho_0^i}{s^i}} \\
  &=\frac{1}{\sum_{i=0}^{s-1}\frac{\rho_0^i}{i!}+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}}
\end{aligned}
$$

设$\sum_{i=0}^{s-1}\frac{\rho_0^i}{i!}=T$，$p_i$可以通过$p_0$推导得：

$$
p_i=\frac{\lambda_0\lambda_1\cdots\lambda_{i-1}}{\mu_1\mu_2\cdots\mu_i}p_0=\left\{
\begin{aligned}
& \frac{\rho_0^i}{i!}p_0=\frac{\rho_0^i}{i!\left(T+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}\right)} & i\leq s \\
& \frac{\rho_0^i}{s!s^{i-s}}p_0=\frac{\rho_0^i}{s!s^{i-s}\left(T+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}\right)} & i > s
\end{aligned}
\right.
$$

当$n \geq s$时，顾客到达系统时需要等待，则有：

$$
p_D=\sum_{i=s}^\infty p_i= \sum_{i=s}^\infty \frac{\rho^i_0}{s!s^{i-s}}p_0 = \frac{\rho^s_0p_0}{(s-1)!(s-\rho_0)}=\frac{\rho^s_0}{(s-1)!(s-\rho_0)T+\rho_0^s}
$$

当$N\leq s$时，系统中没有队列，$L_q=0$，当$N>s$时，队列长度为$N-s$，因此稳态时的平均排队长为：

$$
\begin{aligned}
  L_q&=\sum_{i=s + 1}^\infty (i - s)p_i \\
  &=\sum_{i=s}^\infty (i-s)\frac{\rho^i_0}{s!s^{i-s}}p_0 \\
  &= \frac{\rho^s_0p_0}{s!}\sum_{i=0}^\infty \frac{i\rho_0^i}{s^i} \\
  &= \frac{\rho^s_0p_0}{s!}\sum_{i=1}^\infty \left(\frac{\rho_0}{s}\right)^i\frac{s}{s-\rho_0} \\
  &= \frac{\rho^s_0p_0}{(s-1)!(s-\rho)}\frac{\rho_0/s}{1-\rho_0/s} \\
  &= \frac{\rho^{s+1}_0p_0}{(s-1)!(s-\rho_0)^2}
\end{aligned}
$$

状态为$n$的稳态时系统接受服务的实体数量为：

$$
\left\{
\begin{aligned}
&n & n\leq s \\
&s & n> s
\end{aligned}
\right .
$$

因此，稳态系统中接受服务的实体平均数量为：

$$
\begin{aligned}
  L-L_q&=\sum_{i=0}^s ip_i+\sum_{i=s+1}^\infty sp_i \\
  &=\sum_{i=0}^s \frac{\rho_0^i}{(i-1)!}p_0+s\sum_{i=s+1}^\infty \frac{\rho_0^i}{s!s^{i-s}}p_0 \\
  &= \sum_{i=0}^s \frac{\rho_0^i}{(i-1)!}p_0 + \frac{\rho_0^sp_0}{(s-1)!}\sum_{i=1}^\infty \frac{\rho_0^i}{s^i} \\
  &= \sum_{i=0}^s \frac{\rho_0^i}{(i-1)!}p_0 + \frac{\rho_0^{s+1}p_0}{(s-1)!(s-\rho_0)} \\
  &= \frac{\sum_{i=0}^s \frac{\rho_0^i}{(i-1)!}}{\left(T+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}\right)} + \frac{\rho_0^{s+1}p_0}{(s-1)!(s-\rho_0)} \\
  &= \frac{\rho_0 T+1}{T+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}} + \frac{\rho_0^{s+1}}{(s-1)!(s-\rho_0)T+\rho_0^s} \\
  &= \frac{(\rho_0 T+1)(s-1)!(s-\rho_0) + \rho_0^{s+1}}{(s-1)!(s-\rho_0)T+\rho_0^s}\\
  &= \rho_0 + \frac{(s-1)!(s-\rho_0)}{(s-1)!(s-\rho_0)T+\rho_0^s}
\end{aligned}
$$

顾客的平均逗留时间$W=\frac{L}{\lambda}$：

$$
\begin{aligned}
  W&=\frac{L}{\lambda} \\
  &= \frac{\sum_{i=0}^\infty ip_i}{\lambda} \\
  &= \frac{\sum_{i=1}^s \left(\frac{\rho_0^i}{(i-1)!\left(T+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}\right)}\right) + \sum_{i=s+1}^\infty \left(i\frac{\rho_0^i}{s!s^{i-s}\left(T+\frac{\rho_0^s}{(s-1)!(s-\rho_0)}\right)}\right) }{\lambda} \\
  &= \frac{\frac{T(s-1)!(s-\rho_0)}{T(s-1)!(s-\rho_0) + \rho_0^s} + \frac{\rho_0^{s+1}(s-\rho_0+1)/(s-\rho_0)}{T(s-1)!(s-\rho_0) + \rho_0^s}}{\lambda} \\
  &= \frac{T(s-1)!(s-\rho_0) + \rho_0^{s+1}(s-\rho_0+1)/(s-\rho_0)}{\lambda(T(s-1)!(s-\rho_0) + \rho_0^s)}
\end{aligned}
$$