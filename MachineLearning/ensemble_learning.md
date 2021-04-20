# Ensemble Learning

## 1. Boosting

Boosting 训练基分类器采用串行方式，各个基分类器之间有依赖。

将分类器层层叠加，每一层训练时对前一层分类器分错的样本给予更高的权重。测试时，根据各层分类器的结果加权得到最终结果。

Boosting方法通过聚焦于基分类器分错的样本，减少集成分类器的偏差。

### 1.1 Adaboost


### 1.2 GBDT
在GBDT的迭代中，假设我们前一轮迭代得到的强学习器是$f_{t-1}(x)$, 损失函数是$L(y, f_{t-1}(x))$, 我们本轮迭代的目标是找到一个CART回归树模型的弱学习器ℎ𝑡(𝑥)，让本轮的损失函数$𝐿(𝑦,𝑓_𝑡(𝑥))=𝐿(𝑦,𝑓_{𝑡−1}(𝑥)+ℎ_𝑡(𝑥))$最小。也就是说，本轮迭代找到决策树，要让样本的损失尽量变得更小。

GBDT利用损失函数的负梯度来拟合本轮损失的近似值，进而拟合一个CART回归树。即：
$$ r_{ti} = - [\frac{\partial L(y_i, f(x_i))}{\partial f(x_i)}]_{f(x)=f_{t-1}(x)}$$
利用$(x_i, r_{ti})$,我们可以拟合一颗CART回归树，得到了第t颗回归树。

针对每一个叶子节点里的样本，我们求出使损失函数最小，也就是拟合叶子节点最好的的输出值$c_{tj}$：
$$c_{tj} = argmin_c \sum_{x_i \in R_{tj}} L(y_i, f_{t-1}(x_i)+c)$$

### 1.3 XGBoost
> XGBoost: A Scalable Tree Boosting System

A tree ensemble model uses K additive functions to
predict the output:
$$ \hat{y}_i = \sum_{k=1}^K f_k(x_i)$$
The model is trained in an additive manner. We will need to add $f_t$ to minimize the following objective:
$$ L^{(t)} = \sum_{i=1}^n l(y_i, \hat{y}_i^{(t-1)}+f_t(x_i))+\Omega(f_t)$$
where second term penalize the complexity of model: $\Omega(f) =\gamma T +\frac{1}{2}\lambda ||w||^2$. 
- T: number of leaves
- w: weights in leaves

Use second-order approximation to optimize the objective:
$$ L^{(t)} \simeq \sum_{i=1}^n [l(y_i, \hat{y}_i^{(t-1)})+g_if_t(x_i)+\frac{1}{2}h_if_t^2(x_i)]+\Omega(f_t)$$
where $g_i=\partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$ and $h_i=\partial_{\hat{y}^{(t-1)}}^2 l(y_i, \hat{y}^{(t-1)})$.

For a fixed structure q(x), we can compute the optimal weight $w_j$ of leaf j by:
$$ w_j^* = -\frac{\sum_{i\in I_j}g_i}{\sum_{i \in I_j}h_i +\lambda}$$
And the corresponding optimal loss value:
$$L^{(t)}(q) = -\frac{1}{2}\sum_{j=1}^T\frac{(\sum_{i\in I_j}g_i)^2}{\sum_{i \in I_j}h_i +\lambda} +\gamma T$$
XGBoost uses two additional techniques to further prevent overfitting:

1. shrinkage
2. feature subsampling

Split finding algorithms:
In each iteration, we need to find the best tree structure.

1. Exact Greedy Algorithm
2. Approximation Algorithm
3. Weighted Quantile
4. Sparsity-aware Split Finding


## 2. Bagging

Bagging方法在训练过程中各个基分类器无强依赖，可以并行训练。为了让基分类器之间互相独立，通常将训练集分为若干子集。

Bagging通过对训练样本进行多次采样，训练不同的模型来减少集成分类器的方差。

### 2.1 Random Forest
随机森林是bagging的一个特化进阶版，所谓的特化是因为随机森林的弱学习器都是决策树。所谓的进阶是随机森林在bagging的样本随机采样基础上，又加上了特征的随机选择。


## 3. 结合策略
1. 平均法：用于回归：算术平均法，加权平均法
2. 投票法：用于分类：多数投票法，加权投票法
3. 学习法：不是对弱学习器的结果做简单的逻辑处理，而是再加上一层学习器，也就是说，我们将训练集弱学习器的学习结果作为输入，将训练集的输出作为输出，重新训练一个学习器来得到最终结果。
