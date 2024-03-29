# 确定需求下的库存控制

在持有成本与固定订货成本之间平衡——单次订货量$\bsQ$

## EOQ模型

### 记号

* 需求率$\lambda$，周期长度$T$
* 成本：固定订货成本$K$、边际订货成本$c$、边际持有成本$h$

  > 边际持有成本$h$通常以利率$I$的形式表示，此时有$h = Ic$

* 订货提前期$\tau = 0$
* **不允许缺货**

### 推导

考虑一个订货周期，由于不考虑订货提前量，订货后产品会立即到达，因此为降低持有成本，最优订货方式为库存为零时重新订货。因此订货周期满足$Q = \lambda T$。一个订货周期中的成本为订货成本和库存成本之和，即$C = K + cQ + hQT/2$。

{{ latex_image('imgs/inventory-control-deterministic-demand/eoq-inventory.tex', 'eoq-inventory') }}

单位时间的成本

$$
C(Q) = \frac{C}{T} = \frac{K\lambda}{Q} + \lambda c + \frac{hQ}{2}
$$

对单位时间成本求导，得到

$$
C'(Q) = \frac{h}{2} - \frac{K\lambda}{Q^2}
$$

当单位时间成本最小时，$C'(Q^\ast) = 0$，解得

$$
Q^\ast = \sqrt{\frac{2K\lambda}{h}}
$$

与此对应的最小成本为

$$
C(Q^\ast) = \frac{K\lambda}{Q^\ast} + \lambda c + \frac{hQ^\ast}{2} = \lambda c + \sqrt{2K\lambda h}
$$

### 模型扩充

#### 订货提前期

设订货提前期为$\tau > 0$，首先考虑$\tau \leq T$的情况，由于不允许缺货，在库存提前期内的最低库存应当为零，即$R = \lambda\tau$时应当重新订货，$R$称为重订货点。

当$\tau > T$时，由于模型面对周期性的需求，只需根据提前期$\tau' = \tau\mod T$计算重订货点。

#### 敏感性分析

敏感性分析指$Q^*$的估计偏差对总成本的影响。偏差以$C(Q) / C(Q^\ast)$衡量，为便于分析，设边际订货成本$c = 0$，则总成本的偏差量$C(Q) / C(Q^\ast)$为：

$$
\begin{aligned}
    \frac{C(Q)}{C(Q^\ast)} &= \frac{\frac{K\lambda}{Q}  + \frac{hQ}{2}}{\sqrt{2K\lambda h}} \\
    &= \sqrt{\frac{K\lambda}{2h}}\frac{1}{Q} + \sqrt{\frac{h}{2K\lambda}}Q \\
    &= \frac{1}{2}\left(\frac{Q}{Q^\ast} + \frac{Q^\ast}{Q}\right)
\end{aligned}
$$

#### 允许缺货

当允许缺货时，设缺货成本为$p$，最大缺货量$xQ$，一个周期内库存水平变化如下图所示：

{{ latex_image('imgs/inventory-control-deterministic-demand/penalty-inventory.tex', 'penalty-inventory') }}

成本函数为

$$
C(Q, x) = \frac{C}{T} = \frac{(1-x)^2 Qh + x^2Qp}{2} + \frac{K\lambda}{Q} + \lambda c
$$

分别求$C$关于$Q, x$的偏导数，有

$$
\begin{aligned}
  \frac{\partial C}{\partial Q} &= \frac{(1-x)^2h + x^2p}{2} - \frac{K\lambda}{Q^2} \\
  \frac{\partial C}{\partial x} &= xpQ + (x-1)hQ
\end{aligned}
$$

解方程$\partial C/\partial x =0$得到$x^* = h/(h+p)$，代入方程$\partial C/\partial Q =0$，解得：

$$
Q^* = \sqrt{\frac{2K\lambda}{(1-x)^2h+x^2p}} = \sqrt{\frac{2K\lambda(h+p)}{hp}}
$$

若定义$h' = hp/(h+p)$。则最优订货量转化为类似于EOQ的形式，即$\sqrt{\frac{2K\lambda}{h'}}$

#### 有限生产率模型

在有限生产率模型中，产品通过生产而不是订购获得。产品的生产率为$P > \lambda$，生产线的启动成本为$K$，产品的单位生产成本为$c$。

生产成本（原订货成本）部分的处理与EOQ模型相同。但有限生产率模型的平均库存水平与EOQ模型不同。

* 一个周期中EOQ模型的平均库存水平：$Q/2$
* 一个周期中有限生产率模型的平均库存水平：$Q(P-\lambda)/2P$

{{ latex_image('imgs/inventory-control-deterministic-demand/production-inventory.tex', 'production-inventory') }}

因此有限生产率模型的成本函数为

$$
C(Q) = \frac{C}{T} = \frac{K\lambda}{Q} + \frac{hQ(P-\lambda)}{2P} + \lambda c
$$

最优订货量为

$$
Q^\ast = \sqrt{\frac{2PK\lambda}{h(P-\lambda)}}
$$

若定义$h' = (P-\lambda) / P$，则最优订货量转化为类似于EOQ的形式，即$\sqrt{\frac{2K\lambda}{h'}}$

## 数量折扣模型

在数量折扣模型中，当每个周期的订货量达到一定水平时，会获得边际订货成本的折扣，折扣分为两种类型，即**全量折扣**与**增量折扣**。

* 全量折扣指当订购量超过临界值时，将折扣应用于全部的订购数量上。
* 增量折扣指当订购量超过临界值时，将折扣应用于超过临界值的部分上。

数量折扣模型针对的是**库存成本**的改变，边际订货成本的改变不会影响EOQ模型的最优订货量。

通过数量折扣，可以诱导零售商提高订货批量，从而实现超量库存的转移。

### 全量折扣的求解过程

根据EOQ模型计算出每一个折扣价格$h_i$下对应的最优订货量$Q^*_i$，确定最大可行的最优订货量$Q^\ast = \max Q^\ast_i$。取该折扣点以及高于该折扣点的所有折扣点为候选，即$I = \{i | i\geq \arg\max_i Q^\ast_i\}$。分别比较每个折扣点对应的平均成本，成本最低的$Q$即为最优订货批量。

{{ latex_image('imgs/inventory-control-deterministic-demand/all-unit-discount.tex', 'all-unit-discount') }}

### 增量折扣的求解过程

根据EOQ模型，计算出所有成本曲线最低点对应的$Q$值，并筛选出满足增量折扣约束的订货量，平均成本最低的$Q$即为最优订货批量。

{{ latex_image('imgs/inventory-control-deterministic-demand/incremental-discount.tex', 'incremental-discount') }}

### 短期折扣

短期折扣即生产商只在一个周期中提供折扣。为简化处理，折扣时零售商的购买量$Q_d$为EOQ最优订货量$Q^*$的整数$k$倍。

## 资源约束下的EOQ模型

EOQ模型仅适用于一种产品的最优订货情形，无法处理多种产品需要协调订购的问题。在多种产品的订购场景下，不同的产品有不同的需求率，需要在不同产品的EOQ最优订货量进行平衡。

**模型假设**：部分固定订货成本与产品种类有关——$K_i$，部分固定订货成本与产品种类无关——$K$。

**约束条件**分为资金约束与库存空间约束。如

$$
\left\{
\begin{aligned}
  C&\geq \sum_{i=1}^n c_iQ_i \\
  Q_i^{\mathrm{EOQ}} &= \sqrt{\frac{2K_i\lambda_i}{h_i}}
\end{aligned}
\right.
$$

对于紧约束的情况，将约束写作$\sum_{i=1}^n c_iQ_i = C$，引入拉格朗日算子$\theta$，将残差项与乘子项相加，得到拉格朗日优化的目标函数$C(Q_1, \cdots, Q_n, \theta)$

$$
\min C(Q_1, \cdots, Q_n, \theta) = \sum_{i=1}^n
\left(\frac{h_iQ_i}{2} + \frac{K_i\lambda_i}{Q_i}\right) + \theta\left(\sum_{i=1}^n c_iQ_i - C\right)
$$

最优条件下，有$\partial C/\partial \theta = \partial C/\partial Q_i = 0$，即

$$
\begin{aligned}
  \sum_{i=1}^n c_iQ_i^* - C &= 0 \\
  \frac{h_i}{2} - \frac{K_i\lambda_i}{ {Q_i^*}^2} + \theta c_i &= 0
\end{aligned}
$$

解得$Q_i^*$，代入约束条件即可解得最优的$\theta$

$$
\sum_{i=q}^n c_i\sqrt{\frac{2K_i\lambda_i}{h_i + 2\theta c_i}} = C
$$

不妨设$h_i / c_i = I, \forall i=1, \cdots, n$。则$Q_i^* = \sqrt{\frac{2K_i\lambda_i}{h_i}}\sqrt{\frac{1}{1 + 2\theta / I}}$，注意到$Q_{i}^{\mathrm{EOQ}} = \sqrt{\frac{2K_i\lambda_i}{h_i}}$，则

$$
\left\{
\begin{aligned}
  Q_i^* &= \sqrt{\frac{1}{1 + 2\theta / I}}Q_{i}^{\mathrm{EOQ}} \\
  C &= \sum_{i=1}^n c_iQ_i^*
\end{aligned}
\right.
$$

解得

$$
\theta = \frac{\sum_{i=1}^n \left(c_iQ_i^{\mathrm{EOQ}}\right) - c}{2c / I}
$$

## 多产品EOQ模型

在多产品EOQ模型中，系统需要面对$U = \{1, \cdots, n\}$个产品的需求，每个产品$i$有如下的参数：

* 附加订货成本$K_i$、边际订货成本$c_i$
* 以利率形式表示的库存成本$h_i = I_ic_i$
* 需求率$\lambda_i$
* 不允许缺货

向量化表示的各个参数分别为$\boldsymbol{K}, \boldsymbol{c}, \boldsymbol{h}, \boldsymbol{I}, \boldsymbol{\lambda}$。另外，有全局固定订货成本$K$。在多产品EOQ模型中，假设某次的订货量为$\boldsymbol Q = (Q_i)_{n}$，则订货成本为

$$
\begin{aligned}
  G(\boldsymbol Q) =& K + \sum_{i=1}^n K_i\boldsymbol{1}_{\{Q_i > 0\}} & \text{Setup cost} \\
  &+\sum_{i=1}^n c_iQ_i & \text{Marginal cost}
\end{aligned}
$$

现有三种订货方法

1. 独立订货——每次订购都需要多花费$K$的固定订货成本
2. 完整订货——对于需求率不高的产品，订货过于频繁导致额外花费了$K_i$的附加订货成本
3. 联合订货：不需要订购所有类型的产品

以下对三种订货方法进行讨论

### 独立订货

独立订货下，每种产品按其对应的EOQ订货量进行订货，则平均成本

$$
G^* = \sum_{i=1}^nG_i^* = \sum_{i=1}^n\sqrt{2{K + K_i}\lambda_i h_i}
$$

### 完整订货

完整订货下，每个周期内都需要订购所有产品，设订货量为$\boldsymbol{Q} = T\boldsymbol\lambda$，类比于EOQ模型，可以得到总成本为

$$
G(Q) = \frac{K + \sum_{i} K_i}{T} + \boldsymbol{c}^\top\boldsymbol{\lambda} + \frac{T\boldsymbol{h}^\top\boldsymbol \lambda}{2}
$$

转化为单产品EOQ问题，最优解为

$$
\begin{aligned}
  T^* &= \sqrt{\frac{2\left(K + \sum_{i} K_i\right)}{\boldsymbol{h}^\top \boldsymbol{\lambda}}} \\
  G^* &= \sqrt{2\left(K + \sum_{i} K_i\right)\boldsymbol{h}^\top \boldsymbol{\lambda}} \\
\end{aligned}
$$

### 联合订货

联合订货条件下，每次订货不需包含所有类型的产品，但**需求量最高的产品必然在每个订单中都出现**，因此，首先考虑EOQ模型下产品的订货频率：

$$
n_i = \frac{1}{T_i} = \sqrt{\frac{h_i\lambda_i}{(K + K_i)}}
$$

以订货最频繁的产品$i^\ast = \arg\max\limits_{i} n_i$对应的订货频率$\bar n = n_{i^\ast}$、订货周期$\bar T = T_{i^\ast}$为基准，考虑其他类型产品的订货频率：

$$
m_i = \left\lceil\frac{\bar n}{n_i}\right\rceil
$$

$m_i$表示产品$i$的订购周期为$m_i\bar T_i$，即最频繁订单周期的$m_i$倍，则一个订货周期内的成本为

$$
\begin{aligned}
  G(\boldsymbol Q) =& \frac{1}{T}\left(K + \sum_i\frac{K_i}{m_i}\right) & \text{Setup cost} \\
  &+\frac{h}{2}\sum_{i}\lambda_i m_i & \text{Marginal cost}
\end{aligned}
$$

因此，最优订货周期与最优成本为

$$
\begin{aligned}
  T^* &= \sqrt{\frac{\sum_{i} \lambda_i m_i h}{2\left(K + \sum_i\frac{K_i}{m_i}\right)}} \\
  G^* &= \sqrt{2\left(\sum_{i} \lambda_i m_i h\right)\left(K + \sum_i\frac{K_i}{m_i}\right)}
\end{aligned}
$$
