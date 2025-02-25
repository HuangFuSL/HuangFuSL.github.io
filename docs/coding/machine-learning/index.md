# Machine Learning Glossary

## Topic Subsections

* Statistical Machine Learning
* General Machine Learning
* Deep Learning
* Reinforcement Learning
* Natural Language Processing
* Recommender Systems

## A

### Ablation

**消融实验（Ablation Study）**是一种通过逐步剔除模型的某些组件，来评估组件对模型性能的影响的实验。消融实验常用于评估模型的可解释性，或者验证模型的某些组件对模型性能的贡献。

### A/B Test

**A/B测试（A/B Test）**是一种通过对比两个或多个版本的实验，来评估不同版本的效果的方法。A/B测试通过控制变量，随机分配实验对象接受不同的版本，然后通过假设检验的方法来评估不同版本的效果。常用的假设检验方法有Z检验、T检验、卡方检验等。

### Activation Function

**激活函数（Activation Function）**是神经网络中用于引入非线性因素的函数。常用的激活函数为[sigmoid](#sigmoid-function)、[ReLU](#rectified-linear-unit)等。

[softmax](#softmax-function)严格意义上也算作激活函数，但它常用于神经网络的输出层，将输出值映射到概率空间。

### Action

### Active Learning

**主动学习（Active Learning）**是一类机器学习范式。主动学习首先在一个小规模的标注数据集上训练模型，随后要求模型从未标注数据集上自主选择对提升性能最有价值的数据，交由专家标注，以提升模型对数据的使用效率。主动学习适合于标注数据成本较高，或是有大量未标注数据，或是数据集的标签分布不均匀的情况。但由于主动学习依赖于模型选择标注的样本点，次优的样本选择策略可能会引入[选择偏差](#selection-bias)。

常见的样本选择策略有

* 不确定性采样（Uncertainty Sampling），即选择模型预测结果最不确定的样本进行标注，可以进一步细分为：
    * 最小置信度（Least Confidence），即选择预测概率中最高概率最小的样本
    * 边缘采样（Margin Sampling），即选择预测概率中最高概率和次高概率差最小的样本（接近决策边缘）
    * 熵采样（Entropy Sampling），即选择预测概率分布熵最大的样本
* 预期模型变化（Expected Model Change），即选择对模型影响最大的样本
* 信息增益（Information Gain），即选择最大化模型参数信息增益的样本

### Actor-Critic

### Adam

### Adaptor Tuning

### Advantage

### Adversarial Examples

### Adversarial Training

### Agent (LLM)

### Agent (RL)

### Alignment

### Attention

**注意力机制（Attention Mechanism）**是一种序列建模方式，由Vaswani等人提出[^transformer]。首先，序列被建模成查询（Query）、键（Key）和值（Key）三种表示。通过查询、键的匹配得分，通过[softmax](#softmax-function)为值分配权重，从而实现对序列的建模。其数学表达为：

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{\bsQ\bsK^\top}{\sqrt{d_k}}\right)\bsV
$$

### Attention Mask

### AUC

**Area Under Curve (AUC)**指[ROC曲线](#roc-curve)下的面积，是一类用于评估二分类问题的评价指标，其主要衡量模型区分正样本和负样本的能力。AUC不会受到模型标签不平衡的影响。值为$0.5$时说明模型和随机分类相当，值为$1$时说明模型能够完美分类。

可以遍历所有的预测概率，计算每个概率阈值下的TPR和FPR，使用梯形法计算曲线下的面积。

### Autoencoder

**自编码器（Autoencoder, AE）**是一种数据压缩方式，它通过编码器（encoder）将数据压缩为更低维度的隐向量表示，再尝试用解码器（decoder）复原为原始的数据输入。模型通过[均方误差](#mean-squared-error)最小化低维隐向量重建后的数据和原数据之间的差异，以保证编码器生成的隐向量有重建原始数据所需的必要信息。

相关实现：

* [Autoencoder on MNIST](autoencoder.ipynb)

### Auto-regression

## B

### Bag-of-Words

### Baseline

**基线（Baseline）**是一种用于评估模型性能的方法。基线模型通常是一种简单的模型，用于评估新模型的性能是否优于基线模型。基线模型可以是一个简单的线性模型、随机模型，或是已有的[SOTA](#state-of-the-art)模型。

### Bayesian Optimization

**贝叶斯优化（Bayesian Optimization, BO）**是一类仅依赖于对函数值的观测，寻找函数最值的优化算法。贝叶斯优化算法的核心是通过有限次对函数的观测，对*目标函数*建立概率估计，通过此概率估计找到下一个用于观测的点。优化算法通过不断尝试，借助概率估计找到函数的最优值。贝叶斯算法是一种[主动学习](#active-learning)算法，适合于目标函数为黑盒且计算复杂的情况，如[超参数](#hyperparameter)优化。

常用的对函数建模的方式为[高斯过程](#gaussian-process)。高斯过程通过核函数，假设了目标函数的形状。

相关实现：

* [贝叶斯优化](bayesian-optimization.ipynb)

### Bayesian Preference Ranking

### Beam Search

### Bernoulli Distribution

**伯努利分布（Bernoulli Distribution）**是一种只有两种结果的离散概率分布。参数$p$为成功（$X = 1$）的概率。伯努利分布的概率质量函数为：

$$
f(X = x\mid p) = p^x(1 - p)^{1 - x}
$$

### Bernoulli Trial

**伯努利试验（Bernoulli Trial）**是一种只有两种结果的随机试验，如抛硬币、掷骰子等。伯努利试验的特点是每次试验的结果只有两种可能，成功（概率为$p$）和失败（概率为$1 - p$），服从[伯努利分布](#bernoulli-distribution)$\text{Bernoulli}(p)$。

### BERT

### Beta Distribution

**Beta分布（Beta Distribution）**是一个定义在区间$[0, 1]$上的连续概率分布。Beta分布的概率密度函数为：

$$
f(x\mid\alpha, \beta) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}
$$

其中，$B(\alpha, \beta)$为Beta函数，$\alpha, \beta$为分布的两个参数。Beta分布是二项分布的[共轭先验](#conjugate-prior)。Beta分布$\calB(\alpha, \beta)$的均值为$\frac{\alpha}{\alpha + \beta}$，方差为$\frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$。Beta分布描述了在[博努利试验](#bernoulli-trial)试验中，观测到$\alpha - 1$次成功和$\beta - 1$次失败后，成功概率$p$的分布。

### Bias (Parameter)

### Bias-Variance Trade-off

### Bilingual Evaluation Understudy

### Bootstrap

### Box-Muller Transform

**Box-Muller变换（Box-Muller Transform）**是一种生成服从标准正态分布的随机变量的方法。在使用[逆变换采样](#inverse-transform-sampling)时，我们需要保证目标分布的累积分布的逆函数是初等的。但对于[正态分布](#gaussian-distribution)而言，其累积分布函数的逆函数不是初等函数。Box-Muller变换通过引入极坐标系，利用极坐标系的对称性简化积分过程。具体的数学推导和代码实现参见[Jupyter Notebook](box-muller-transform.ipynb)

### Byte Pair Encoding

## C

### Catastrophic Forgetting

### Causal Decoder

### Chain-of-Thoughts

### Classification

### Click-Through Rate

### Coefficient of Determination

### Cold-Start Problem

### Collaborative Filtering

### Conditional Random Field

### Confidence Interval

### Conjugate Prior

### Contrastive Learning

**对比学习（Contrastive Learning, CL）**是一类通过强调*正样本对*（相似的两个样本）和*负样本对*（不相似的两个样本）之间差异性的[自监督学习](#self-supervised-learning)方式。它通过编码器生成原始数据在低维隐空间内的表示，通过拉近正样本对的距离，拉远负样本对之间的距离，来学习到原始样本在隐向量空间内的表示。损失函数定义为

$$
\calL = y\Vert x_1 - x_2\Vert^2 + (1 - y)\max(m, \Vert x_1 - x_2\Vert^2)
$$

$x_1, x_2$为样本，当两者相似（如来自同一张图片的多个变换，或属于同一个类别）时，$y = 1$，否则$y = 0$。另一种常用的损失函数为

$$
\calL = \max(0, \Vert x - x^\plus\Vert^2 - \Vert x - x^-\Vert^2 + m)
$$

其中$x, x^\plus$为相似的样本，$x^-$为和$x, x^\plus$不相似的样本。

### Controlled Decoding

### Convolution Neural Network

### Cosine Similarity

### Covariate Shift

### Cross Attention

### Cross Entropy

**交叉熵（Cross Entropy）**是两个分布之间的差异度量。从信息论的角度出发理解，交叉熵衡量的是用分布$Q$来表示分布$P$的平均编码长度。由于$P$和$Q$的分布不同，用$Q$来编码$P$的信息会导致信息损失，即平均编码长度要高于$P$的[熵](#entropy)。

$$
\text{CE}(P, Q) = -\int P(x)\log Q(x)dx
$$

交叉熵可以由[KL散度](#kl-divergence)推导而来，下式中$H(P)$为分布$P$的[熵](#entropy)。

$$
\begin{aligned}
\text{KL}(P||Q) &= \int P(x)\log\frac{P(x)}{Q(x)}dx \\
&= \int P(x)\log P(x)dx - \int P(x)\log Q(x)dx \\
&= H(P) - \text{CE}(P, Q)
\end{aligned}
$$

交叉熵损失是用于分类任务的[损失函数](#loss-function)，其中$P$为真实分布（经验分布），$Q$为模型预测分布，最小化交叉熵等价于最小化$\text{KL}(P\Vert Q)$。

* 对于二分类任务，交叉熵定义为：

    $$
    \calL = -\frac{1}{n}\sum_{i=1}^{n} y_i\log p_i + (1 - y_i)\log(1 - p_i)
    $$

    其中，$y_i$是第$i$个样本的真实标签，$p_i$是模型预测第$i$个样本为正样本的概率，$n$是样本数量。

* 对于多分类任务，交叉熵定义为：

    $$
    \calL = -\frac{1}{n}\sum_{i=1}^{n}\sum_{j=1}^{m} \boldsymbol1_{\{y_i = j\}}\cdot\log p_{ij}
    $$

    其中，$y_{i}$是第$i$个样本的真实标签，$p_{ij}$是模型预测第$i$个样本为第$j$类的概率，$n$是样本数量，$m$是类别数量。

另外，从似然角度出发，交叉熵反映了模型预测概率的负对数[似然](#likelihood)。

### Cross Validation

### Curse of Dimensionality

## D

### Data Augmentation

### Data Imbalance

### Data Parallelism

### Decision Boundary

### Decision Tree

* [决策树](decision-tree.ipynb)

### Decoder

### Decoder-only

### Deep Q Network

### Diffusion Model

**扩散模型（Diffusion Model）**，全称扩散概率模型（Diffusion Probabilistic Model），是一类基于[变分推断](#variational-inference)和[马尔可夫链](#markov-chain)的模型。最初由Jascha等人于2015年提出[^dpm]，由Jonathan等人改进[^ddpm]。

### Direct Preference Optimization

### Discriminative Model

### Discriminator

### Disentangle

### Dropout

### Dynamic Programming

## E

### Early Stopping

### Embedding

### Encoder

### Encoder-Decoder

### Encoder-only

### End-to-End

**端到端（End-to-End）**是一种将整个系统作为一个整体进行优化的方法。在机器学习中，端到端学习指的是将输入数据直接映射到输出数据的过程，而**不需要人工进行特征提取等特征工程**。端到端学习的优点是无需人工干预，可以直接从训练数据中学习到模型所需的特征。端到端学习的缺点是模型的复杂度较高，训练时间较长；模型的可解释性较差；要求更高质量的训练数据。

如：transformer模型[^transformer]最初的设计用于机器翻译任务，将输入的源语言句子直接映射到目标语言句子，不需要人工提取特征。

### Entropy

### Environment

### Euclidean Distance

### Evidence Lower Bound

### Expectation-Maximization Algorithm

**EM算法（Expectation-Maximization Algorithm）**是一种用于优化含有隐变量或参数$\theta$的概率模型的一类方法。设概率模型为$P(X, Z; \theta)$和输入数据$x$，我们可以通过最大化对数似然$\log P(X = x;\theta)$的方式优化模型参数$\theta$，然而，由于隐变量$Z$的存在（$\log P(x; \theta) = \log\int_{Z} P(x, z; \theta)$），该对数似然难以优化。因此，EM算法采取交替的方式进行优化：

* Expectation步骤：根据当前估计的参数$\theta^{(t)}$，在隐变量的条件分布$Z \mid X = x, \theta^{(t)}$下估计对数似然$\log P(x, z;\theta)$的期望
    $$
    Q(\theta, \theta^{(t)}) = \mathbb E_{z\sim Z \mid X = x, \theta^{(t)}} \log P(x, z;\theta)
    $$
* Maximization步骤：优化该对数似然，更新参数$\theta$
    $$
    \theta^{(t + 1)} = \arg\max_{\theta} Q(\theta, \theta^{(t)})
    $$

以上步骤不断重复，直至参数收敛。EM算法可以保证模型参数收敛到局部最优解，但无法保证全局最优性。

### Experience Replay

### Experimental Distribution

### Exploration-Exploitation Trade-off

### Exposure Bias

## F

### F1

### Factorization Machine

### Feedback Loop

### Feedforward Neural Network

### Few-shot Learning

### Few-shot Prompting

## G

### Gated Recurrent Unit

### Gaussian Distribution

**高斯分布（Gaussian Distribution）**，又称正态分布（Normal Distribution），是一种连续概率分布。

* 均值为$\mu$，方差为$\sigma^2$的一元高斯分布的概率密度函数为：

    $$
    f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x - \mu)^2}{2\sigma^2}}
    $$

    标准正态分布的均值为0，方差为1，概率密度函数简写作$\phi(x)$，累积分布函数简写作$\Phi(x)$。

* 均值为$\boldsymbol\mu$，方差为$\Sigma$的多元高斯分布的概率密度函数为：

    $$
    f(\bsx) = \frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}e^{-\frac{1}{2}(\bsx - \boldsymbol\mu)^\top\Sigma^{-1}(\bsx - \boldsymbol\mu)}
    $$

高斯分布满足如下性质：

1. 若随机变量$X$服从高斯分布$\mathcal N(\mu, \sigma^2)$，经过线性变换$Y = aX + b$后，$Y$仍然服从高斯分布$\mathcal N(a\mu + b, a^2\sigma^2)$。
2. 若随机变量$X_1, X_2$相互独立且分别服从高斯分布$\mathcal N(\mu_1, \sigma_1^2)$和$\mathcal N(\mu_2, \sigma_2^2)$，则$X_1 + X_2$服从高斯分布$\mathcal N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$。
3. 多元高斯分布的条件分布依然是高斯分布。设随机变量$X = (X_1, X_2)$服从多元高斯分布$\mathcal N(\mu, \Sigma)$，其中$\mu = (\mu_1, \mu_2)$，$\Sigma = \begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}$，则给定$X_1 = x_1$后，$X_2$的条件分布为：

    $$
    (X_2\mid X_1 = x_1) \sim \mathcal N(\mu_2 + \Sigma_{21}\Sigma_{11}^{-1}(x_1 - \mu_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})
    $$

### Gaussian Process

**高斯过程（Gaussian Process，GP）**是将[多变量高斯分布](#gaussian-distribution)推广到无限维度$\mathcal X\subseteq \mathbb R^n$的概率分布。它的核心思想是用概率的方法描述函数在每一个点处的分布，从而能够对任意位置函数值进行推断和不确定性量化。总体来看，高斯分布研究的是函数的概率分布，常用于[贝叶斯优化](#bayesian-optimization)、[回归任务](#regression)等。

具体地，对于$\bsx = \{x_1, \ldots, x_n\}\subseteq \mathcal X$，高斯分布假设函数在这些点的观测值$Y_1 = f(x_1), \ldots, Y_n = f(x_n)$是随机变量，并且服从某个受自变量$\bsx$影响的多元高斯分布$\mathcal N(\mu(\bsx), \Sigma(\bsx))$。其中，$\mu(\bsx)$为均值函数，$\Sigma(\bsx)$为协方差函数。

高斯过程的核心是[核函数](#kernel-function)。核函数定义了自变量之间的相似性，通过协方差矩阵反映函数值之间的相关性。高斯分布的条件分布依然是高斯分布，借助于均值函数和协方差矩阵，我们就可以推断函数在新位置的分布。

相关实现：

* [高斯过程](gaussian-process.ipynb)

### Generalized Linear Models

* [线性模型](linear-models.ipynb)

### Generative Adversarial Network


**生成对抗网络（Generative Adversarial Networks, GAN）**是一种生成模型，它由两个神经网络组成：生成器（Generator）和判别器（Discriminator）。生成网络的目标是从样本空间$\mathcal X$中生成尽可能逼真的样本$\mathbb P_g$，而判别网络的目标是尽可能准确地区分真实样本的分布$\mathbb P$和生成样本的分布$\mathbb P_g$。两个网络的训练目标相互对抗，在对抗训练中，生成器可以学习到如何从随机噪声中重建样本。GAN的训练过程是一个[零和博弈](#zero-sum-game)的过程，生成器和判别器的损失函数是相互对抗的。

在最初的GAN模型[^gan]中，判别器使用[二分类交叉熵](#cross-entropy)作为损失函数，生成器使用判别器输出的负对数概率作为损失函数。通过优化二分类交叉熵，判别器提供了生成器分布和真实分布的[JS散度](#kl-divergence)的下界，从而使生成器生成的样本更加逼真。

当生成器分布和真实分布相差较大时，JS散度面临梯度消失的问题，导致训练不稳定、模式崩塌等问题，表现为生成器生成的样本质量较差。为解决这一问题，后续的GAN模型提出了多种改进方法，如使用[Wasserstein距离](#wasserstein-distance)衡量生成器分布和真实分布的差异[^wgan]，使用[梯度惩罚](#gradient-penalty)的方式辅助估算Wasserstein距离[^wgan-gp]。

对于有明确分类标签的样本，可以将分类标签作为生成器和判别器的条件输入，得到条件生成对抗网络（Conditional GAN）[^cgan]。

相关实现：

* [GAN on MNIST](gan.ipynb)
* [Wasserstein GAN on MNIST](wgan.ipynb)
* [Conditional GAN on MNIST](cgan.ipynb)

### Generative Model

### Generator

### Gibbs Sampling

### Gradient Boosted Trees

### Gradient Clipping

### Gradient Exploding

### Gradient Vanishing

### Graph

### Graph Convolution

### Graph Neural Network

### Group Relative Policy Optimization

### Grouped Query Attention

## H

### Hadamard product

### Hinge Loss

### Hyperparameter

## I

### Importance Sampling

### In-Context Learning

### Inner Product

### Instruct Tuning

### Inverse Transform Sampling

## J

### Jaccard Coefficient

### Jacobian Matrix

### Jensen Inequality

## K

### Kernel Function

### K-Means

### K-Nearest Neighbor

### KL Divergence

**KL散度（Kullback-Leibler Divergence, KL Divergence）**是两个概率分布之间的差异度量。KL散度的定义为：

$$
\text{KL}(P\Vert Q) = \int P(x)\log\frac{P(x)}{Q(x)}\mathrm dx = \mathbb E_P\left[\log\frac{P(x)}{Q(x)}\right]
$$

KL散度不是对称的，即$\text{KL}(P\Vert Q)\neq\text{KL}(Q\Vert P)$。KL散度可以理解为用分布$Q$来近似分布$P$时的信息损失。$P$本身的信息量为分布$P$的[熵](#entropy)$\mathbb E_P[-\log P(x)]$，用$Q$来近似$P$时的信息量为[交叉熵](#cross-entropy)$\mathbb E_P[-\log Q(x)]$，两者的差异即为KL散度。为了保证KL散度的非负性，KL散度的定义中通常要求$Q$的支撑集包含$P$的支撑集，即$Q(x) = 0$时，$P(x) = 0$。

???+ proof "KL散度的非负性"

    对于任意两个概率分布$P, Q$，KL散度$\text{KL}(P\Vert Q)\geq 0$，且当且仅当$P = Q$时，KL散度等于0。

    注意到$-\log x$是凸函数，由[Jensen不等式](#jensen-inequality)可得：

    $$
    \mathbb E_P\left[\log\frac{P(x)}{Q(x)}\right] = \mathbb E_P\left[-\log\frac{Q(x)}{P(x)}\right] \geq -\log\mathbb E_P\left[\frac{Q(x)}{P(x)}\right] = -\log 1 = 0
    $$

**JS散度（Jensen-Shannon Divergence）**是KL散度的对称形式，定义为：

$$
\text{JS}(P\Vert Q) = \frac{1}{2}\text{KL}(P\Vert M) + \frac{1}{2}\text{KL}(Q\Vert M)
$$

其中，$M = \frac{1}{2}(P + Q)$为$P$和$Q$的均值分布。JS散度同样满足非负性，且当且仅当$P = Q$时，JS散度等于0。

### Knowledge Distillation

### Knowledge Graph

**知识图谱（Knowledge Graph）**是一种用于表示实体之间关系的[图](#graph)结构[^knowledge-graph]。知识图谱中的节点表示实体，边表示实体之间的关系。知识图谱常用于知识表示、知识推理等任务。

两个节点$L, R$和连接他们的边$E$构成一个三元组$(L, E, R)$，表示$L$和$R$之间存在关系$E$。如三元组$(\text{北京}, \text{首都}, \text{中国})$表示“北京是中国的首都”。

知识图谱的构建可以通过自动化的方式，如从文本中抽取实体和关系，或者通过人工标注的方式。

### KV-Cache

## L

### Label Smoothing

### Language Model

### Lasso Regression

### Latent Dirichlet Allocation

### Latent Variable Model

### Learning Rate

### Learning to Rank

### Likelihood

### Linear Discriminative Analysis

### Linear Regression

### Lipschitz Continuity

### Llama

### Logisitic Regression

### Logit

### Long-Short Term Memory

### Loss Function

**损失函数（Loss Function）**是用来评价模型预测值与真实值之间的差异的函数。可以借助随机梯度下降等优化算法来调整模型的参数，使得损失函数的值最小。对于不同的机器学习任务，损失函数的选择也不同。常用的损失函数有：

* 回归任务：[平均绝对误差](#mean-absolute-error)、[均方误差](#mean-squared-error)或[均方根误差](#root-mean-squared-error)
* 多分类任务：[交叉熵](#cross-entropy)
* 二分类任务：[二分类交叉熵](#cross-entropy)

### Low Rank Adaptation

## M

### Markov Chain

### Markov Chain Monte Carlo

### Markov Decision Process

### Matrix Factorization

### Maximum Likelihood Estimation

### Maximum A Posteriori

### Mean Absolute Error

**平均绝对误差（Mean Absolute Error, MAE）**，又称L1 Loss。计算预测值与真实值之间的绝对差的均值。是在[回归任务](#regression)中使用的[损失函数](#loss-function)。

$$
\begin{aligned}
L(y, t) &= \frac{1}{2} \sum_{i=1}^{n} |y_i - t_i| \\
\frac{\partial L}{\partial y_i} &= \begin{cases}
1, & y_i > t_i \\
-1, & y_i < t_i \\
0, & y_i = t_i
\end{cases}
\end{aligned}
$$

其中，$y_i$ 是模型对第$i$个样本的预测值，$t_i$ 是第$i$个样本真实值，$n$ 是样本数量。

### Mean Reciprocal Rank

**平均倒数排名（Mean Reciprocal Rank, MRR）**是用于评估排序模型的指标。衡量的是模型在给定查询时，返回的第一个相关文档的排名的倒数。MRR的计算公式为：

$$
\text{MRR} = \frac{1}{n}\sum_{i=1}^{n}\frac{1}{\text{rank}_i}
$$

其中，$n$是查询的数量，$\text{rank}_i$是第$i$个查询的第一个相关文档的排名。MRR指标强调相关文档的排名位置，鼓励模型将相关文档排在前面。

### Mean Squared Error

**均方误差（Mean Squared Error, MSE）**，又称L2 Loss，是[回归任务](#regression)中常用的[损失函数](#loss-function)。它计算的是预测值与真实值之间的平方差的均值。

$$
\begin{aligned}
L(y, t) &= \frac{1}{2} \sum_{i=1}^{n} (y_i - t_i)^2 \\
\frac{\partial L}{\partial y_i} &= y_i - t_i
\end{aligned}
$$

其中，$y_i$ 是模型对第$i$个样本的预测值，$t_i$ 是第$i$个样本真实值，$n$ 是样本数量。

[最小二乘法](#ordinary-least-squares)即是通过均方误差进行优化的线性回归方法。

### Meta Learning

**元学习（Meta Learning）**，又称为“学会学习”（Learning to Learn），是一种机器学习范式。元学习针对机器学习模型难以适应新任务或新场景的问题。其核心目标是让模型具备快速适应新任务或新场景的能力，尤其是在数据稀缺的情况下。通过学习多个任务中的共性知识（元知识），使模型在面对新任务时仅需少量样本即可高效调整参数。元学习通常分为如下三个范式：

1. **Optimization-based Meta Learning**：通过在多个任务上迭代优化模型参数，使模型只需要少量的迭代更新，即具备适应新任务的能力。
2. **Memory-based Meta Learning**：通过记忆历史任务的信息，使模型在面对新任务时能够检索利用相关历史任务的知识辅助适应新的任务。
3. **Black-box Adaptation Meta Learning**：元模型直接为子任务的模型生成参数。
4. **Metric-based Meta Learning**：通过度量学习的方式，学习任务之间的相似性，从而在新任务上快速适应。

### METEOR

### Metric

### Metroplis-Hastings Sampling

### Mixture-of-Experts

### Model Parallelism

### Model Pruning

### Monte Carlo Sampling

### Multi-armed Bandit

### Multi-Head Attention

### Multi-Head Latent Attention

### Multi-Layer Perceptron

### Mutual Learning

## N

### Naive Bayes

### Norm

### Normalization

### Normalized Discounted Cumulated Gain

## O

### Offline

### One-hot Encoding

### Online

### Ordinary Least Squares

### Overfitting

### Overflow

## P

### Padding

### Parameter Efficient Fine-Tuning

**参数高效微调（Parameter Efficient Fine-Tuning）**是一种用于[预训练模型](#pretrained-model)的微调方法。传统的微调方法是直接在预训练模型的基础上添加一个分类头，然后在目标任务上进行[端到端](#end-to-end)的微调。此类微调方法在预训练模型参数较多时，由于优化器需要保存所有训练参数的中间状态，训练的空间和时间开销较大。为解决这一问题，出现了参数高效微调方法。这类方法在预训练模型的基础上添加一个小的参数集，然后锁定预训练模型的参数，只训练新添加的参数集。通过减少需要微调的参数数量，参数高效微调实现了在利用预训练模型的基础上，减少微调的计算量和存储需求。

常见的参数高效微调方法有[LoRA](#low-rank-adaptation)、[Adaptor Tuning](#adaptor-tuning)等。

### Pearson Correlation Coefficient

### Perplexity

### Policy

### Policy Gradient

### Pooling

### Positional Embedding

### Positive-Unlabeled Learning

**正样本和无标签学习（Positive-Unlabeled Learning，PU Learning）**是一类特殊的[有监督学习](#supervised-learning)方式。和二分类问题不同，PU Learning的标签划分并不可靠，无标签的样本中既可能存在负样本，也可能存在正样本。PU Learning的核心问题是如何借助正样本的信息，识别出无标签样本中可能存在的正样本。

### Precision

### Prefix Decoder

### Prefix Tuning

### Pretrained Model

### Prompt

### Prompt Tuning

### Proximal Preference Optimization

## Q

### Quantization

## R

### Random Forest

### Recall (Metric)

### Recall (Recommender System)

### Recall-Oriented Understudy for Gisting Evaluation

### Recommender System

### Rectified Linear Unit

**ReLU（Rectified Linear Unit）**是一种常用的[激活函数](#activation-function)，由Hinton等人在2010年提出[^relu]。ReLU函数将输入值小于0的部分置为0，大于0的部分保持不变。

$$
\begin{aligned}
\text{ReLU}(x) &= \max(0, x) \\
\text{ReLU}'(x) &= \begin{cases}
1, & x > 0 \\
0, & x \leq 0
\end{cases}
\end{aligned}
$$

### Recurrent Neural Network

### Residual (Regression)

### Residual Connection

### Reward

### Regression

### Regularization

### Reinforcement Learning

**强化学习（Reinforcement Learning）**是一种机器学习范式，用于解决顺序决策问题。在强化学习中，智能体（Agent）通过与环境（Environment）的交互，学习到在某个状态下采取某个动作的策略，以最大化累积奖励。强化学习的核心是建模智能体与环境之间的交互，以及智能体如何根据环境的反馈调整策略。

强化学习的核心概念包括：状态（State）、动作（Action）、奖励（Reward）、策略（Policy）、价值函数（Value Function）、模型（Model）等。

### Reinforcement Learning from Human Feedback

### Rejection Sampling

**拒绝采样（Rejection Sampling）**是一种从给定的概率密度函数$f(x)$所对应的概率分布中采样的方法。其核心思想是从一个容易采样的分布（提议分布，proposal distribution，概率密度函数为$g(x)$）中采样样本，通过选择性接受和拒绝采样结果，控制采样结果接近于期望的分布。从离散概率分布的概率密度概念出发，将概率密度在某一点取值的含义延伸到连续概率分布上，如果能保证$f(x) / g(x)$是一个介于$[0, 1]$之间的概率，则按照概率$f(x) / g(x)$接受采样结果即可。然而，$f(x) / g(x)$并不能保证是一个概率，此时可以引入一个系数$M$满足$f(x)\leq Mg(x)$对于所有的$x\in \{x\mid g(x) > 0\}$成立。系数$M$存在的必要条件是提议分布$g(x)$的域包含目标分布$f(x)$的域。具体的代码实现参见[Jupyter Notebook](rejection-sampling.ipynb)。

拒绝采样的缺点在于采样效率不高。当系数$M$非常大时，会拒绝大量的样本。

### Representation Learning

### Retrieval Augmented Generation

### Ridge Regression

### ROC Curve

**ROC曲线（ROC Curve**，全称为Receiver operating characteristic curve，是一个反映二分类任务性能的曲线。在二分类任务中，模型通常输出样本为正例的概率$P(y = 1 | x)$，由外部设定一个阈值$t$，规定概率高于$t$的样本为正例，低于$t$的样本为负例。阈值$t$可以在区间$[0, 1]$上自由选择，在选择的过程中，[第一类错误](#type-i-error)和[第二类错误](#type-ii-error)会相继出现。定义**真正例率（True Positive Rate, TPR）**为所有正例（TP+FN）中被预测为正例（TP）的比例，**假正例率（False Positive Rate, FPR）**为所有负例（FP+TN）中被预测为正例（FP）的比例。ROC曲线即为在$[0, 1]$上移动，以TPR为$y$轴、FPR为$x$轴，作出的曲线。

ROC曲线开始于$(0, 0)$，结束于$(1, 1)$。直线$y = x$表示模型的预测是随机的，曲线中离左上角越近的点预测准确率越高。有预测效果的模型，其ROC曲线高于$y = x$；折线$(0, 0) - (0, 1) - (1, 1)$表示模型能够完美分类。

ROC曲线下的面积称为[AUC](#auc)，是用于衡量分类器分类效果的评价指标。

### Root Mean Squared Error

### Recall-Oriented Understudy for Gisting Evaluation

## S

### Selection Bias

### Semi-Supervised Learning

### Self Attention

### Self-Supervised Learning

### Sequence Mask

### Sequence-to-Sequence

### Sigmoid Function

**Sigmoid函数**是一个将输入值压缩到0到1之间的函数，用$\sigma$表示。Sigmoid函数常用于二分类问题中，将输出值映射到概率空间。Sigmoid也常作为[激活函数](#activation-function)，用于引入非线性因素。

$$
\begin{aligned}
\sigma(x) &= \frac{1}{1 + e^{-x}} \\
\sigma'(x) &= \sigma(x)(1 - \sigma(x))
\end{aligned}
$$

Sigmoid函数在输入值较大或较小时，梯度会接近于0，导致[梯度消失](#gradient-vanishing)问题。

### Simulated Annealing

### Softmax Function

Softmax函数是一个将输入值压缩到0到1之间的函数，常用于多分类问题中，将模型在多个分类上的预测评分映射到在多个分类上的概率分布，所有类别的概率之和为1。

$$
\begin{aligned}
\text{softmax}(\bsz)_i &= \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}} \\
\text{softmax}'(\bsz)_i &= \text{softmax}(\bsz)_i(1 - \text{softmax}(\bsz)_i)
\end{aligned}
$$

相对应的，softmin函数是softmax函数的对称函数，用于最小化输出值，$\text{softmin}(\bsz) = \text{softmax}(-\bsz)$。

Softmax函数在输入值较大或较小时，梯度会接近于0，导致[梯度消失](#gradient-vanishing)问题。另外，输入值过大可能会导致[上溢](#overflow)问题。

### Speculative Sampling

### State-of-the-Art

**State of the Art**指当前最先进的模型或方法，能够在特定给定的任务或数据集上取得最好的性能。

### Stochastic Gradient Descent

### Supervised Fine-Tuning

### Supervised Learning

### Support Vector Machine

## T

### Term Frequency-Inverse Document Frequency

### Token

### Topic Model

### Transfer Learning

### Transformer

### Type-I Error

**第一类错误（Type-I Error）**指统计模型或机器学习模型错误地将负例视为正例，或者错误地*拒绝原假设*，即**False Positive (FP)**。

### Type-II Error

**第二类错误（Type-II Error）**指统计模型或机器学习模型错误地将正例视为负例，或者错误地*接受原假设*，即**False Negative (FN)**

## U

### Unsupervised Learning

## V

### Value Function

### Variational Autoencoder

相关主题[^vae-tutorial]：

* [Autoencoder](#autoencoder)

### Variational Distribution

### Variational Inference

### Vector Quantization

## W

### Wasserstein Distance

## X

### XGBoost

## Z

### ZeRO

### Zero-Shot Learning

### Zero-Shot Prompting

### Zero Sum Game

[^cgan]: M. Mirza and S. Osindero, “Conditional generative adversarial nets,” 11 2014.
[^dpm]: Sohl-Dickstein, J., Weiss, E. A., Maheswaranathan, N., and Ganguli, S. Deep unsupervised learning using nonequilibrium thermodynamics. In Proceedings of the 32nd International Conference on International Conference on Machine Learning - Volume 37 (2015), ICML’15, JMLR.org, pp. 2256–2265.
[^ddpm]: Ho, J., Jain, A., and Abbeel, P. Denoising diffusion probabilistic models. In Advances in Neural Information Processing Systems (2020), H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, Eds., vol. 33, Curran Associates, Inc., pp. 6840–6851.
[^gan]: I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Ben- gio, “Generative adversarial nets,” in Advances in Neural Information Processing Systems (Z. Ghahra- mani, M. Welling, C. Cortes, N. Lawrence, and K. Weinberger, eds.), vol. 27, Curran Associates, Inc., 2014.
[^knowledge-graph]: Aidan Hogan, Eva Blomqvist, Michael Cochez, Claudia D’amato, Gerard De Melo, Claudio Gutierrez, Sabrina Kirrane, José Emilio Labra Gayo, Roberto Navigli, Sebastian Neumaier, Axel-Cyrille Ngonga Ngomo, Axel Polleres, Sabbir M. Rashid, Anisa Rula, Lukas Schmelzeisen, Juan Sequeda, Steffen Staab, and Antoine Zimmermann. 2021. Knowledge Graphs. ACM Comput. Surv. 54, 4, Article 71 (May 2022), 37 pages. https://doi.org/10.1145/3447772
[^relu]: V. Nair and G. E. Hinton, “Rectified linear units improve restricted boltzmann machines,” in Proceedings of the 27th international conference on machine learning (ICML-10), pp. 807–814, 2010.
[^transformer]: A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” 06 2017.
[^vae-tutorial]: D. P. Kingma and M. Welling, “An introduction to variational autoencoders,” Foundations and Trends in Machine Learning: Vol. 12 (2019): No. 4, pp 307-392, 06 2019.
[^wgan]: M. Arjovsky, S. Chintala, and L. Bottou, “Wasserstein gan,” 01 2017.
[^wgan-gp]: I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. Courville, “Improved training of wasserstein gans,” 04 2017.