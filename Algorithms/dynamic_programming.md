# DP

动态规划 与分治方法相似，都是通过组合子问题来求解原问题。动态规划常应用于子问题重叠的情况，避免了分治方法不必要的重复计算。

动态规划仔细安排子问题求解顺序，并将结果保存下来。即付出额外内存空间来节省计算时间。

1. 带备忘的自顶向下法
2. 自底向上法

## 背包问题
```
def knapsack(values, weights, w):
    dp = [[0 for _ in range(len(values))] for _ in range(w+1)]
    for i in range(1, len(values)+1):
        for j in range(1, w+1):
            if j < weights[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
    return dp[len(values)][w]
  
```
## LCS (Longest Common Subsequence)


# 贪心算法
有时我们可以无需求解所有子问题就能找到最优解。
因此，贪心算法通常自顶向下进行计算，做出一个选择，然后求解剩下的子问题。

## 霍夫曼编码
霍夫曼贪心算法构造出字符的最优二进制表示。（只考虑前缀码，即没有任何编码是其他编码的前缀，可简化解码过程）。
```
def huffman(C):
    Q = C # 以freq为关键字的优先队列
    n = len(C)
    for i in range(1, n):
        x = extract_min(Q)
        y = extract_min(Q)
        # 在每一步中，频率最低的两棵树进行合并
        z = Node()
        z.left = x
        z.right = y
        z.freq = x.freq + y.freq
        insert(Q, z)
    return extract_min(Q)
```