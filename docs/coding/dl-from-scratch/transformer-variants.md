# Transformer变种

Transformer变种主要包含如下几种：

* 改变transformer的注意力计算方式，如Linformer、Reformer等；
* 改变transformer的位置编码方式；
* 改变transformer的归一化层；
* 改变transformer的激活函数；
* 部分语言模型（如Llama）使用的线性层不带偏置；
* 改变transformer归一化层的位置，是先归一化再加残差（Pre-Norm），还是先加残差再归一化（Post-Norm）。

## BERT

BERT的结构特点为：

* encoder-only，即使用Bidirectional self-attention；
* 使用绝对位置编码；

## Llama

Llama的结构特点为：

* decoder-only，即使用Causal self-attention；
* 全部使用不带偏置的线性层；
* 在FFN中使用SiLU配合门控；
* 使用RoPE位置编码；
* 使用RMSNorm归一化层。归一化方式为pre-norm，即先进行归一化，再进行注意力或者全连接计算，然后加残差。