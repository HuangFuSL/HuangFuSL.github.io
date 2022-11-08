# REDRL: A review-enhanced Deep Reinforcement Learning model for interactive recommendation

## Introduction

* Tradition RS: 静态策略
* Interactive RS: 根据用户反馈对推荐策略进行动态更新

IRS的实现方式

1. Multi-armed bandit (MAB)
    * 在exploration和exploitation之间进行平衡
    * 缺点：假设用户的选择偏好是静态的
2. Reinforcement learning (RL)
    * RL在长期的决策与优化过程中可以取得较好的效果
    * 缺点：样本空间过大、只考虑用户与商品间的评分关系（数据稀疏性的问题）、没有考虑推荐历史对用户偏好的影响（表现为只使用隐层最后一个输出作为特征表示）
    * 解决方案
        1. Deep Deterministic Policy Gradient (DDPG)

            use the idea of collaborative filtering, highly relys on the accuracy of clustering

        2. 使用用户的评论数据提高推荐算法的效果

Highlights

1. Text reviews: based on a pretrained representation model
2. Formalize the decision process
3. Multi-head attention
4. Meta-path in user-item bipartite

## Related work

1. Collaborative filtering
    * User-based or item-based
    * Cold-start problem
    * Approaches: ML - based on dimensionality reduction
    * Approaches: DL
        1. MLP
        2. Auto-Encoders
        3. Memory network
        4. CNN
        5. RNN and attention architecture
2. Reinforcement learning
    * MAB
    * RL - Formalize the problem to MDP
    * Relies only on rating information
3. Review information
    * Deep Cooperative Neural Networks
    * PARL
    * CARL

## Problem Definition

马尔可夫决策过程可以由$\left(\mathcal S, \mathcal A, \mathcal P, \mathcal R, \gamma\right)$表示，其中：

1. **样本空间** $\mathcal S$ ， $s_t\in \mathcal S$表示用户在$t$时刻有 **正向** 评价的商品集合。
2. **决策空间** $\mathcal A$ ， $a_t\in \mathcal A$表示推荐系统在$t$时刻为用户推荐的商品
3. **回报** $\mathcal R$ ， $r(s_t, a_t): \mathcal S\times \mathcal A\rightarrow \mathcal R$ 表示推荐系统在 $s_t$ 状态下为用户推荐$a_t$时用户的反馈
4. **转移概率** $\mathcal P$ ，本文中，当用户对商品 $i$ 给出正向评价时，将状态空间更新为 $s_{t+1} = s_t \cup \{i\}$ ，否则为 $s_{t+1} = s_t$
5. **贴现率** $\gamma$ ，平衡短期收益与长期收益的影响

需要得出一个最优策略 $\pi: \mathcal S\rightarrow \mathcal P(\mathcal A)$ ，即最大化决策过程的累积收益。

## Reference

```bibtex
@article{LIU2023118926,
title = {REDRL: A review-enhanced Deep Reinforcement Learning model for interactive recommendation},
journal = {Expert Systems with Applications},
volume = {213},
pages = {118926},
year = {2023},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2022.118926},
url = {https://www.sciencedirect.com/science/article/pii/S0957417422019443},
author = {Huiting Liu and Kun Cai and Peipei Li and Cheng Qian and Peng Zhao and Xindong Wu},
keywords = {Recommender system, Deep reinforcement learning, Review analysis}
}
```