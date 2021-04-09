# 字符串匹配

设文本是一个长度为n的数组T，模式是一个长度为m的数组P。如果模式P在文本T中出现，且偏移为s，则称s为有效偏移，否则为无效偏移。字符串匹配问题就是找到所有的有效偏移。

## 朴素字符串匹配算法

```
def naive_string_matcher(T, P):
    n = len(T)
    m = len(P)
    for i in range(n):
        if P == T[i:i+m]:
            print(i) 
```

Complexity: O((n-m+1)m)

## Rabin-Karp 算法


## 有限自动机
一个有限自动机是一个五元组：$(Q, q, A, \Sigma, \delta)$
- $Q$ 是 状态的有限集合
- $q\in Q$ 是 初始状态
- $A\subseteq Q$ 是一个特殊的接受状态集合
- $\Sigma$ 是有限输入字母表
- $\delta$ 是转移函数，为一个从$Q*\Sigma$到$Q$的函数

有限自动机开始状态为q，每次读取输入字符串的一个字符a，状态由q变为$\delta(q,a)$。

对于给定长度为m的模式P，相应的字符串匹配自动机定义如下：
$Q = {0, 1, ..., m}$, 0 为初始状态。
$\delta(q, a)= max{(k: P_k是P_qa的后缀)}$

```
# f: transition function
# C: all available characters
def compute_transition_function(P, C):
    m = len(P)
    for q in range(0, m):
        for c in C:
            k = min(m+1, q+2)
            while not is_suffix(P[0:k], P[0:q]+[c]):
                k -= 1 
            f(q, c) = k
    return f

def finite_automation_matcher(T, f, m):
    n = len(T)
    q = 0
    for i in range(n):
        q = f(q, T[i])
        if q == m:
            print(i-m)
```

## KMP (Knuth-Morris-Pratt)
KMP会用到一个辅助函数$\pi$

$\pi$包含模式与其自身的偏移进行匹配的信息。

$$ \pi(q) = max(k: k<q \quad and \quad P_k \ \ is \ \ suffix \ \ of \ \  P_q)$$

```
def compute_prefix_function(P):
    m = len(P)
    pi = [0 for _ in range(m+1)]
    k = 0
    for q in range(1, m):
        while k > 0 and P[q] != P[k]:
            k = pi[k]

        if P[q] == P[k]:
            k += 1

        pi[q] = k

    return pi 

def KMP_matcher(T, P):
    n, m = len(T), len(P)
    pi = compute_prefix_function(P)
    q = 0
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q]

        if P[q] == T[i]:
            q += 1

        if q == m:
            print(i-m+1)
            q = pi[q]
```


