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


## Node2Vec

> to learn a mapping of nodes to a low-dimensional space
of features that maximizes the likelihood of preserving network neighborhoods of nodes.

for a node u, we define $N_S(u)$ a network neighborhood of node u generated through a neighborhood sampling strategy S.

Generally, there are two extreme sampling strategies for
generating neighborhood sets $N_S(u)$ of k nodes:
1. BFS: The neighborhood NS is restricted to nodes which are immediate neighbors of the source.
2. DFS: The neighborhood consists of nodes sequentially sampled at increasing distances from the source node.

**homophily**: nodes that are highly interconnected and belong to similar network clusters or communities should be embedded closely together.

**structural equivalence**: nodes that have similar structural roles in networks should be embedded
closely together.

the neighborhoods sampled by BFS lead to embeddings
that correspond closely to structural equivalence. 

DFS can explore larger parts of the network as it can move further away from the source node u. In DFS, the sampled nodes more accurately reflect a macro-view of the neighborhood which is essential in inferring communities based on homophily.