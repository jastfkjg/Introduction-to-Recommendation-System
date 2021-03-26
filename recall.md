# 召回 Recall

- 主要介绍i2i相关算法

## Expectation

We note 

$N_{XY}$: the number of customers who bought both item X and item Y.

$E_{XY}$: the expected num of customers who bought both X and Y.

If we assume X-buyers have the same probability of buying Y as the general population: $P(Y) =\frac{|Y \quad buyers|}{|all\quad buyers|}$. Then $E_{XY} = |X \quad buyers| * P(Y)$ will be the expected number of customers who bought both X and Y.

However, for almost any two items X and Y, customers who bought X will be much more likely to buy Y then the general population.

Sampling a random purchase doesn't give a uniform probability of selecting customers. For heavy buyers, they have much more probability to be selected when we look for all customers who have bought X.

This means we can't ignore who bought X when we try to estimate how many X-buyers we would expect to randomly buy Y.

For a customer who purchased X, we can estimate his probability of buying Y:
$$ 1 - (1-P_Y)^{|c|}$$
where $|c|$ represents the number of non-X purchases made by him. Therefore, we can calculate the expected num of customers who bought both X and Y:

$$ E_{XY}=\sum_{c\in X} [1- (1-P_Y)^{|c|}]$$

<div align="center">
<img src="images/expectation.png" width = "500">
</div>

$N_{XY}-E_{XY}$ gives an estimate of the number of non-random co-ocurrences.

$[N_{XY}-E_{XY}]/E_{XY}$ gives the percent difference from the expected random co-occurrences. 

if we use $N_{XY}-E_{XY}$ as score $S_{XY}$, it will be biased toward popular Y's.

if we use $[N_{XY}-E_{XY}]/E_{XY}$ as score, it will make it too easy for the low-selling items to have high scores.

Therefore, $S_{XY}=[N_{XY}-E_{XY}]/\sqrt{E_{XY}}$ strikes a balance.

## Wbcos

## Node2Vec

见 embedding.

## Swing
> 两个用户同时点击商品i和j，如果两个用户共同购买的物品越少，则swing的对应的结构就越强，即物品i与j相似性越高。

## U2i

## ranki2i

## pd2i 
重定向：用户N天内点击，收藏，购买过的商品。


## btb

## 其他非个性化或弱个性化召回

1. hot
2. c2i
3. d2i



