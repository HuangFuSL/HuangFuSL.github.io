# 大模型推理

在推理阶段，大模型根据输入的文本序列，不断预测输入文本的下一个词，直到预测出结束符号为止。不过，在预训练阶段中，不包含对bos（begin of sentence）和eos（end of sentence）的预测。所以，如果使用基座模型，模型会不断输出token。

## KV-cache

把输入序列重新输出LLM，预测下一个单词推理流程的计算效率非常低，原因在于每一次预测都需要对整个序列计算注意力得分。然而，由于每一个token的表示只依赖于前面的token，在推理阶段，我们不必重算前边的token，只需要存储前边的token的KV表示即可。只需用最后一个token的Q计算注意力即可得到对下一个token的预测。这种技术即称为KV缓存。包含KV缓存的推理过程分为两个阶段，即缓存填充（prefill）阶段和解码（decode）阶段。

!!! note "为何只需要KV-cache而不需要Q-cache"

    假设输入序列经过$QKV$计算后的序列为$S^Q, S^K, S^V$，并且可以拆分为列向量表示：

    $$
    \begin{aligned}
    S^Q &= \begin{bmatrix} Q_1 & Q_2 & \cdots & Q_n \end{bmatrix} \\
    S^K &= \begin{bmatrix} K_1 & K_2 & \cdots & K_n \end{bmatrix} \\
    S^V &= \begin{bmatrix} V_1 & V_2 & \cdots & V_n \end{bmatrix}
    $$

    注意力得分矩阵为

    $$
    \begin{bmatrix}
    Q_1K_1 & Q_1K_2 & \cdots & Q_1K_n \\
    Q_2K_1 & Q_2K_2 & \cdots & Q_2K_n \\
    \vdots & \vdots & \ddots & \vdots \\
    Q_nK_1 & Q_nK_2 & \cdots & Q_nK_n
    $$

    由于decoder的causal mask限制，最终计算的表示为

    $$
    \begin{aligned}
    O_1 &= \sum_{i=1}^1 \text{softmax}(Q_1K_i)V_i \\
    O_2 &= \sum_{i=1}^2 \text{softmax}(Q_2K_i)V_i \\
    \end{aligned}
    $$

    也即，每个位置的表示，只依赖该位置的Q，和该位置及之前的K和V。因此预测下一个单词时，不需要重新计算KV，将KV存储下来即可。

将输入序列输入LLM时，首先进行缓存填充，保存下所有层的KV-cache，然后进行解码，不断预测下一个单词，并记录预测单词的KV表示。对于decoder的每一层，都需要保存一个KV-cache，每一层cache的大小为$2\times N\times L\times D$。对于长序列，KV-cache的大小会非常大。