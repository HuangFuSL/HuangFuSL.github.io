# 确定需求下的库存控制

在持有成本与固定订货成本之间平衡——单次订货量$Q$

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

## 有限生产率模型

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
Q^\ast = \sqrt{\frac{PK\lambda}{2h(P-\lambda)}}
$$

若定义$h' = (P-\lambda) / P$，则最优订货量转化为类似于EOQ的形式，即$\sqrt{\frac{K\lambda}{2h'}}$

### 模型扩展

#### 多种产品的有限生产率模型

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