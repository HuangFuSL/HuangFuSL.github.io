# 随机需求下的库存控制

优化目标：最小化成本的数学期望

## 单周期——报童模型

报童模型是单周期下的库存控制问题

### 记号

* $c_o$表示超额订货成本，$c_u$表示缺货成本
* $f(\cdot), F(\cdot)$分别为需求的概率密度函数与概率分布函数
* $Q$为订货量
* $x^+ = \max\{x, 0\}$

### 推导

报童模型的成本函数为

$$
G(Q, D) = c_o\max\{0, Q-D\} + c_u\max\{0, D-Q\}
$$

$G(Q, D)$是随机变量$D$的函数，因此也是随机变量，对$D$取期望，有

$$
\begin{aligned}
    C(Q) &= E(G(Q, D) | Q) \\
    &= \int_{0}^\infty G(Q, D)f(x)\mathrm dx \\
    &= \int_{0}^Q c_o(Q-x)f(x)\mathrm dx + \int_Q^\infty c_u(x-Q)f(x)\mathrm dx \\
\end{aligned}
$$

当$C(Q)$取极小值时，有$\frac{\mathrm dC}{\mathrm dD} = 0$，即

$$
\begin{aligned}
    \frac{\mathrm dC}{\mathrm dQ} &= c_o\int_0^Q f(x)\mathrm dx + c_u\int_Q^\infty -f(x)\mathrm dx \\
    &= c_oF(Q) - c_u(1-F(Q)) \\
    &= 0
\end{aligned}
$$

验证：$\frac{\mathrm d^2 C}{\mathrm dQ^2} = (c_o + c_u)f(Q) > 0$，因此为极小值点。此时$F(Q^*) = c_u / (c_o + c_u)$。

称$c_u / (c_o + c_u)$为**关键比例**（crucial ratio）

### 单周期模型扩展

#### 离散需求的最优策略

确定$\max_{Q_0}, \min_{Q_1}$满足$Q_1 > Q_0$且$F(Q_0) < c_u / (c_u + c_o) < F(Q_1)$，此时$Q_1$即为最优的$Q^*$。即高于最优关键比例的最小关键比例对应的$Q$

#### 存在初始库存$u$

$u$的存在不影响$Q^*$，因此，订货量$Q'$满足

$$
Q^{*\prime} = \max\{Q^*-u, 0\}
$$

## 周期检查模型

在周期检查模型中，首先不考虑固定订货成本$K$的影响。需求分为多个周期，每个周期的需求独立同分布。

### 记号

* 剩余周期数为$n$
* 每个周期的需求独立同分布，需求的概率密度函数为$f(\cdot)$，概率分布函数为$F(\cdot)$。
* 周期之间的贴现率$\alpha$表示
* 不考虑订货提前期，$L=0$
* $y_i$表示第$i$期结束时的库存，$y_0$表示期初库存
* $C_n(y_0)$表示第$n$期总期望贴现成本的最小值

$$
C_n(y_0) = \min_{y\geq y_0}\left\{L(y) - cy_0 + \alpha\int_{0}^\infty C_{n-1}[t(y, x)]f(x)\mathrm dx\right\}
$$

## 连续检查模型：(Q, R)模型

在连续检查模型中，需要区分**库存位置**与**库存水平**的概念

* 库存位置（Inventory Position），指目前持有的库存总量加上处于订货提前期的库存量
* 库存水平（Inventory Level），指目前持有的库存总量

### 模型设定及推导

$(Q, R)$模型有如下设定

1. 每次订货的固定成本为$K$，边际订货成本为$c$，订货提前期为$\tau$；
2. **订货提前期内的**需求$D$在时间上连续，在数量上服从均值为$\mu$、标准差为$\sigma$的某个概率分布$f(\cdot), F(\cdot)$；$\lambda$为单位时间的期望需求率；
3. 单位时间的边际库存成本为$h = Ic$（式中$I$为利率）、缺货成本$p$；
4. 模型的决策变量为重订货点$R$、与订货量$Q$：当库存水平降低至$R$时，订购$Q$单位的库存。受订货量$Q$的影响，订货周期$T$满足$Q = \lambda T$

$(Q, R)$模型考虑如下来源的成本：

1. 订货成本：每次订购$Q$单位的库存，总成本为$K + cQ$；

   $$
   \frac{K + cQ}{T} = \frac{K\lambda}{Q} + c\lambda
   $$

2. 缺货成本：首先计算每个周期内的期望缺货量$n(R)$，有

   $$
   n(R) = E(\max(D - R, 0)) = \int_R^\infty (x-R)f(x)\mathrm dx
   $$

   根据$n(R)$，即可得到一个订货周期$T$时间的平均缺货成本$\lambda n(R)p/Q$

3. 库存成本：一个周期内期望的库存水平变化为线性，当库存水平降至$R$后重新订货，期望库存继续下降，直至降低至$R - \lambda\tau$时订单到达，单位时间内的库存成本为

   $$
   h\left(\frac{Q}{2} + R - \lambda\tau\right)
   $$

根据如上分析，单位时间内的期望成本为

$$
\begin{aligned}
G(Q, R) &= h\left(\frac{Q}{2} + R - \lambda\tau\right) + \frac{K\lambda}{Q} + \frac{p\lambda n(R)}{Q} \\
&= \frac{hQ}{2} + \lambda(K + pn(R))\frac{1}{Q} + hR - h\lambda\tau
\end{aligned}
$$

$(Q, R)$模型的目标即为求解出使得$G(Q, R)$最小的$Q, R$。

### 求解

可以使用迭代的方式逼近$(Q, R)$模型的最优解，分别对$G$求$Q, R$的偏导数，有

$$
\begin{aligned}
    \frac{\partial G}{\partial Q} &= \frac{h}{2} - \lambda (K + pn(R))\frac{1}{Q^2} \\
    \frac{\partial G}{\partial R} &= h + \frac{\lambda p n'(R)}{Q} \\
    &= h - \frac{\lambda p(1-F(R))}{Q}
\end{aligned}
$$

迭代过程从EOQ模型的最优解$Q_{\mathrm{EOQ}}^* = \sqrt{\frac{2K\lambda}{h}}$开始，求出使得$G$最优的$R$值，再将$R$代入求出最优的$Q$值，如此循环，$Q, R$即逼近最优的$Q^*, R^*$取值，最优解满足如下方程：

$$
\begin{aligned}
    Q &= \sqrt{\frac{2\lambda (K + pn(R))}{h}} \\
    F(R) &= 1 - \frac{hQ}{\lambda p}
\end{aligned}
$$

### (Q, R)模型的相关指标：服务水平

类似于周期检查模型，在连续检查模型中也可以定义第一类服务水平与第二类服务水平等指标。

#### 第一类服务水平

第一类服务水平指在订货提前期中不发生缺货的概率，用$\alpha$表示。则有$\alpha = F(R)$。求解满足第一类服务水平条件的$(Q, R)$系统，可以按照如下步骤进行

1. 求解满足$F(R) = \alpha$的$R$值
2. $Q$值取EOQ最优值$\sqrt{\frac{2K\lambda}{h}}$即可

#### 第二类服务水平

第二类服务水平指满足的需求占总需求的比例比例，用$\beta$表示，由于$n(R)$为订货提前期中的期望缺货量，则有$n(R)/Q = 1 - \beta$。根据$F(R) = 1 - \frac{hQ}{\lambda p}$，可得

$$
p = \frac{Qh}{\lambda(1 - F(R))}
$$

将其代入$Q = \sqrt{\frac{2\lambda (K + pn(R))}{h}}$，整理得到

$$
hQ^2 - \frac{2hn(R)}{1-F(R)}Q - 2K\lambda = 0
$$

解得

$$
Q = \frac{n(R)}{1 - F(R)} + \sqrt{\frac{2K\lambda}{h} + \left(\frac{n(R)}{1-F(R)}\right)^2}
$$

又根据第二类服务水平，有

$$n(R) = (1-\beta)Q$$

联立即得，也可使用迭代方式求解。

### 模型简化

当需求服从正态分布$N(\mu, \sigma)$时，可以使用正态分布的标准损失函数$L(z)$简化$n(R)$的计算

$$
n(R) = \sigma L\left(\frac{R-\mu}{\sigma}\right) = \sigma L(z)
$$