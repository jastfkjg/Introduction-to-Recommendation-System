# 特征工程

## 特征预处理

**归一化 (Normalization)** ： 将所有特征统一到一个大致相同的数值区间。
1. 线性函数归一化：$X_{norm} = \frac{X - X_{min}}{X_{max}- X_{min}}$
2. 零均值归一化: $z=\frac{x-\mu}{\sigma}$
   
## 特征表示

One-hot
Word Embedding

### Word2Vec

1. CBOW
2. Skip-gram
   
CBOW 目标是根据上下文出现的词语来预测当前词的生成概率。
Skip-gram 是根据当前词来预测上下文中各词的生产概率。


## 过拟合

降低过拟合风险的方法：
1. 增加训练数据：数据扩充，增广（规则，缩放，GAN）
2. 降低模型复杂度： 减少网络层数，剪枝，减特征
3. 正则化，L1，L2，FRTL
4. 集成学习：多模型集成



