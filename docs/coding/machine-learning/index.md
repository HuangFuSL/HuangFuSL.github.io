# Machine Learning Glossary

## A

### Ablation

### A/B Test

### Activation

**激活函数（Activation function）**是神经网络中用于引入非线性因素的函数。常用的激活函数为Sigmoid函数、ReLU函数等。

* [激活函数](activation.md)

### Action

### Active Learning

### Adaptor Tuning

### Agent (LLM)

### Agent (RL)

### Attention

**注意力机制（Attention Mechanism）**是一种序列建模方式。首先，序列被建模成查询（Query）、键（Key）和值（Key）三种表示。通过查询、键的匹配得分，为值分配权重，从而实现对序列的建模。其数学表达为：

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{\bsQ\bsK^\top}{\sqrt{d_k}}\right)\bsV
$$

### AUC

### Autoencoder

**自编码器（Autoencoder, AE）**是一种数据压缩方式，它通过编码器（encoder）将数据压缩为更低维度的隐向量表示，再尝试用解码器（decoder）复原为原始的数据输入。模型通过最小化低维隐向量重建后的数据和原数据之间的差异，以保证编码器生成的隐向量有重建原始数据所需的必要信息。

* [Autoencoder](autoencoder.ipynb)

### Auto-regression

## B

### Baseline

### Bayesian Optimization

**贝叶斯优化（Bayesian Optimization, BO）**是一类仅依赖于对函数值的观测，寻找函数最值的优化算法。贝叶斯优化算法的核心是通过有限次对函数的观测，对*目标函数*建立概率估计，通过此概率估计找到下一个用于观测的点。优化算法通过不断尝试，借助概率估计找到函数的最优值。贝叶斯算法是一种[主动学习](#active-learning)算法，适合于目标函数为黑盒且计算复杂的情况，如[超参数](#hyperparameter)优化。

常用的对函数建模的方式为[高斯过程](#gaussian-process)。高斯过程通过核函数，假设了目标函数的形状。

* [算法流程](bayesian-optimization.ipynb)

### Bayesian Preference Ranking

### Bernoulli Distribution

### BERT

### Beta Distribution

### Bilingual Evaluation Understudy

### Bootstrap

## C

### Chain-of-Thoughts

### Classification

### Click-Through Rate

### Cold-Start Problem

### Collaborative Filtering

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

### Convolution

### Cross Attention

### Cross Entropy

### Cross Validation

## D

### Data Parallelism

### Decision Boundary

### Decision Tree

* [决策树](decision-tree.ipynb)

### Decoder

### Diffusion Model

### Direct Preference Optimization

### Discriminative Model

### Discriminator

### Dropout

## E

### Embedding

### Encoder

### Entropy

### Environment

### Evidence Lower Bound

### Experimental Distribution

### Exploration-Exploitation Trade-off

### Exposure Bias

## F

### F1

### Factorization Machine

### Feedback Loop

### Few-shot Learning

### Few-shot Prompting

## G

### Gated Recurrent Unit

### Gaussian Distribution

### Gaussian Process

* [高斯过程](gaussian-process.ipynb)

相关主题：

* [Bayesian Optimization](#bayesian-optimization)

### Generalized Linear Models

* [线性模型](linear-models.ipynb)

### Generative Adversarial Network

* [生成对抗网络](gan.ipynb)
* [WGAN](wgan.ipynb)
* [Conditional GAN](cgan.ipynb)

### Generative Model

### Generator

### Gradient Boosted Trees

### Grouped Query Attention

## H

### Hinge Loss

### Hyperparameter

## I

### In-Context Learning

## K

### Kernel Function

### K-Means

### K-Nearest Neighbor

### KL Divergence

### Knowledge Distillation

### KV-Cache

## L

### Language Model

### Latent Dirichlet Allocation

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

### Low Rank Adaptation

## M

### Markov Decision Process

### Matrix Factorization

### Maximum Likelihood Estimation

### Maximum A Posteriori

### Mean Absolute Error

### Mean Squared Error

### Mixture-of-Experts

### Model Parallelism

### Multi-armed Bandit

### Multi-Head Attention

### Multi-Layer Perceptron

## N

### Naive Bayes

### Norm

### Normalization

### Normalized Discounted Cumulated Gain

## O

### Offline

### One-hot Encoding

### Online

### Overfitting

## P

### Perplexity

### Policy

### Pooling

### Positional Embedding

### Precision

### Prompt

### Prompt Tuning

### Proximal Preference Optimization

## Q

### Quantization

## R

### Random Forest

### Recall

### Reward

### Recommender System

### Rectified Linear Unit

### Recurrent Neural Network

### Regression

### Regularization

### Reinforcement Learning

### Reinforcement Learning from Human Feedback

### Retrieval Augmented Generation

### ROC Curve

### Root Mean Squared Error

### Recall-Oriented Understudy for Gisting Evaluation

## S

### Selection Bias

### Semi-Supervised Learning

### Self Attention

### Self-Supervised Learning

### Sigmoid Function

### Softmax Function

### State-of-the-Art

### Supervised Fine-Tuning

### Supervised Learning

### Support Vector Machine

## T

### Topic Model

### Transformer

## U

### Unsupervised Learning

## V

### Variational Autoencoder

相关主题：

* [Autoencoder](#autoencoder)

### Variational Distribution

## W

### Wasserstein Distance

## Z

### Zero-Shot Learning

### Zero-Shot Prompting
