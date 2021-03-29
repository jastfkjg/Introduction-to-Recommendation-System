# Probability

## 大数定理 (Law of the large numbers)

当随机事件发生的次数足够多时，随机事件发生的频率趋近于预期的概率。即对于独立事件而言，样本数足够多时，其平均概率接近于期望概率。

## 中心极限定理 (Central Limit Theorem)

随机变量$x_1, x_2, ...,x_n$独立同分布，其均值和方差为$\mu, \sigma^2$。当n很大时，有

$$\frac{\sum_{i=1}^n x_i - n\mu}{\sqrt{n}\sigma} \sim N(0,1)$$

即这n个随机变量之和近似服从正太分布$N(n\mu, n\sigma^2)$。