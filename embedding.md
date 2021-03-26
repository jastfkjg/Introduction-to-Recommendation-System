# Embedding

## Word2Vec
https://zhuanlan.zhihu.com/p/33799633

### Skip-gram
> To find word representations that are useful for predicting the surrounding words. 

$$ max \sum_t \sum_i logp(w_{t+i}|w_t)$$

The basic Skip-gram formulation defines $p(w_{t+i} |w_t)$using the softmax function:
$$ p(w_o|w_i) = \frac{exp(v_{w_o}^Tv_{w_i})}{\sum_w^W v_wv_{w_i}}$$

$v$ is the vector representation of word $w$, and W is the number of words in the vocabulary. This formulation is impractical because the cost of computing
$∇log p(w_o|w_i)$ is proportional to W, which is often large.

Two solutions:

1. Hierarchical softmax:
    输出层从原始模型的利用softmax计算概率值改为了利用Huffman树计算概率值。
2. Negative sampling:
   把语料中的一个词串的中心词替换为别的词，构造语料中不存在的词串作为负样本。
   每次让一个训练样本仅仅更新一小部分的权重参数，从而降低梯度下降过程中的计算量。  
   使用 一元模型分布 (unigram distribution) 来选择 negative words，一个单词被选作 negative sample 的概率跟它出现的频次有关，出现频次越高的单词越容易被选作negative words。
   对于小规模数据集，建议选择 5-20 个 negative words，对于大规模数据集选择 2-5个 negative words.

### CBOW

> 根据源词上下文词汇来预测目标词汇


## Item2Vec

Item2vec中把用户浏览的商品集合等价于word2vec中的word的序列，即句子。同样利用负采样得到每个商品的embedding representation，商品之间两两计算cosine相似度即为商品的相似度。

## DeepWalk
在由物品组成的图结构上进行随机游走，产生大量物品序列，再将这些物品序列作为训练样本输入word2vec进行训练。


## Node2Vec

> to learn a mapping of nodes to a low-dimensional space
of features that maximizes the likelihood of preserving network neighborhoods of nodes.

for a node u, we define $N_S(u)$ a network neighborhood of node u generated through a neighborhood sampling strategy S.

Generally, there are two extreme sampling strategies for
generating neighborhood sets $N_S(u)$ of k nodes:
1. BFS: The neighborhood NS is restricted to nodes which are immediate neighbors of the source.
2. DFS: The neighborhood consists of nodes sequentially sampled at increasing distances from the source node.

**homophily**: nodes that are highly interconnected and belong to similar network clusters or communities should be embedded closely together. （同质性：距离相近的点embedding应近似）



**structural equivalence**: nodes that have similar structural roles in networks should be embedded closely together. （结构性：结构上相似的点embedding应相似）

the neighborhoods sampled by BFS lead to embeddings
that correspond closely to structural equivalence. 

DFS can explore larger parts of the network as it can move further away from the source node u. In DFS, the sampled nodes more accurately reflect a macro-view of the neighborhood which is essential in inferring communities based on homophily.

结构性：BFS
同质性：DFS

node2vec通过控制节点间的跳转概率来控制BFS和DFS的倾向性。

从节点v跳转到下一节点x的概率：
$$\pi_vx = \alpha_pq(t,x)w_vx$$

$$ \alpha_{pq}(t,x)=
    \left\{ 
    \begin{array}{lr} 
    \frac{1}{p} \quad if d_{tx}=0 & \\
    1 \quad if d_{tx}=1 & \\
    \frac{1}{q} \quad if d_{tx} = 2
    \end{array} 
    \right. $$

其中t表示v的前一节点，$d_{tx}$ 表示节点t到节点x的距离。

p越小，随机游走返回节点t的可能性就越高，表达网络的结构性越强。
q越小，随机游走走到远方节点的可能性就越大，表达网络的同质性越强。

通常，同质性相同的物品为同品类，同属性，经常被一起购买。而结构性相同的物品则是各个品类的爆款或一些最佳凑单商品等。


## 局部敏感哈希

Embedding可以作为召回层，计算方法是Embedding向量间的内积运算。但需要遍历所有物品向量，时间复杂度高。

局部敏感哈希(Locality Sensitive Hashing, LSH)基本思想是让相邻的点落入同一个桶内，搜索时只需在一个桶，或相邻的几个桶中进行搜索即可。

将高维空间的点映射到低维空间，原本相近的点在低维空间中肯定依然相近，但原本远离的点则有一定概率变成相近的点。

可以用内积操作构建局部敏感哈希桶，设v是高维空间的一个Embedding向量，x是一个随机生成的同维映射向量，通过内积可映射至一维空间：
$$ h_x(v) = \lfloor \frac{vx+b}{w} \rfloor $$

其中w为桶宽，b可避免分桶边界固化。

实际中，通常采用多个哈希函数进行分桶，再考虑用“与”，“或”操作生成最终的候选集。
