# 预备知识

## 概率空间

当一个试验的结果无法预先确定时，称该实验为**随机试验**。随机试验可能出现的所有结果集合构成样本空间$\Omega$，每个可能的结果称为样本点$\omega$。$\Omega$的子集构成的集合称为**集类**$\mathcal F$。

!!! note "可测空间"

    设$\mathcal F$为由$\Omega$的某些子集构成的非空集类，若满足以下条件：

    1. 若$A\in \mathcal F$，则$A^C = \Omega - A\in \mathcal F$。
    2. 若$A_n\in \mathcal F$，则$\bigcup\limits_{n=1}^\infty A_n \in \mathcal F$

    称$\mathcal F$为$\sigma$域，$(\Omega, \mathcal F)$为可测空间。