# 重排 及 相关精排后策略

## 多样性

- 召回多样性：
  1. 基于CF的算法容易推荐热门商品 -> 热度降权，时间衰减
  2. 多路召回
  3. 利用EE选择不同类别的商品集 (UCB, TS, EXP3)

- 重排多样性：
  1. 打散策略 (类型曝光降权，打散窗口)
  2. 长尾加权（提升冷门商品权重，如用逆用户频率加权）
  3. MMR，DPP

### MMR 
$$ MMR = argmax(\lambda Sim(D_i, Q) - (1-\lambda) Sim(D_i, D_j))$$


### DPP
https://zhuanlan.zhihu.com/p/72202739

DPP (Determinantal Point Process) 通过最大后验概率估计，找到商品集中相关性和多样性最大的子集，从而作为推荐给用户的商品集。


## LTR

