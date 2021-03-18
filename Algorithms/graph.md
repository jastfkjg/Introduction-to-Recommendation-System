# 图

## 图的表示
1. 邻接链表
2. 邻接矩阵

## 图搜索算法
### 1. 广度优先搜索
广度优先算法 需要在发现所有距离源节点为k的所有节点后，才会发现距离源节点为k+1的其他节点。

```
import queue
def bfs(G, start):
    """
    0: 未被访问过
    1: 已被访问过，但邻接点未被完全访问
    2: 已被访问，且邻接点都被访问
    """
    nodes = [0 for _ in range(len(G))]
    distances = [float("inf") for _ in range(len(G))]
    previous = [-1 for _ in range(len(G))]

    nodes[start] = 1
    distances[start] = 0
    previous[start] = -1

    deque = queue.deque
    deque.append(start)
    while deque:
        u = deque.popleft()
        for i in range(len(G[u])):
            if G[u][i] != 0:
                if nodes[i] == 0:
                    nodes[i] = 1
                    distances[i] = distances[u] + 1
                    previous[i] = u
                    deque.append(i)
        nodes[u] = 2

```

Kahn算法：利用bfs和入度 有向图找环/拓扑排序：
```
def bfs_topological_sort(n, edges):
    G = [[] for _ in range(n)]
    degrees = [0 for _ in range(n)]
    for (i, j) in edges:
        G[i] = j
        degrees[j] += 1
    queue = []
    for i in range(n):
        if degrees[i] == 0:
            queue.append(i)
    topological_sort = []
    while queue:
        n = queue.pop(0)
        topological_sort.append(n)
        for j in G[n]:
            degrees[j] -= 1
            if degrees[j] == 0:
                queue.append(j)
    
    if len(topological_sort) == n:
        # 图中无环，返回拓扑排序
        return topological_sort
    else:
        # 图中有环，返回空
        return []
```
   
### 2. 深度优先搜索
深度优先搜索 总是对最近才发现的节点的出发边进行探索，直到该节点的所有出发边都被发现为止。一旦节点v的所有出发边都被发现，则回溯到v的前驱节点，继续搜索前驱节点的出发边。
```
def dfs(G):
    nodes = [0 for _ in range(len(G))]
    previous = [-1 for _ in range(len(G))]

    time = 0
    for i in range(len(G)):
        if nodes[i] == 0:
            dfs_visit(G, i)

def dfs_visit(G, i):
    time = time + 1
    i.d = time
    nodes[i] = 1
    for j in range(len(G[i])):
        if G[i][j] != 0:
            if nodes[j] == 0:
                previous[j] = i 
                dfs_visit(G, j)
    nodes[i] = 2
    time += 1
    i.f = time
```
dfs 通过节点上色检测有向图是否有环，并根据节点dfs结束时间来确定拓扑排序：
```
def dfs_topological_sort(n, edges):
    G = [[] for _ in range(n)]
    colors = [0 for _ in range(n)]
    stack = []
    for i in range(n):
        if colors[i] == 0:
            if dfs(i, G, colors, stack):
                return []
    return stack[::-1]

def dfs(i, G, colors, stack):
    # 如果存在环，返回True，stack记录节点完成顺序，是拓扑排序的逆序
    if colors[i] == 1:
        # 1: visiting, 说明存在环
        return True
    if colors[i] == 2:
        return False
    
    colors[i] = 1
    for j in G[i]:
        if dfs(j, G, colors, stack):
            return True
    
    colors[i] = 2
    stack.append(i)

    return False
```

对于无向图找环：

1. 并查集
2. dfs上色 + （记录前驱点 或 删除遍历过的边）
3. bfs上色 + （记录前驱点 或 删除遍历过的边）

**拓扑排序** 是有向无环图中所有节点的一种线性次序，满足如下条件：如果图中包含边(u,v)，则节点u在拓扑排序中处于节点v的前面。
```
def topological_sort(G):
    1. call dfs(G) to compute finishing time v.f for each vertex v
    2. as each vertex is finished, insert it onto the front of a linked list
    3. return the linked list 
```

**强连通分量** 是有向图的一个最大节点集合，该集合中任意两个节点可以互相到达。

```
def strongly_connected_components(G):
    1. call dfs(G) to compute finishing time v.f for each vertex v
    2. compute G^T  # G^T 即G对其有向边进行反向获得
    3. call dfs(G^T) in order of decreasing u.f as computed in line 1
    4. output the vertices of each tree in the depth-first forest formed in line 3 as a seperate strongly connected component
```



## 最小生成树 (MST)
最小生成树： 联通所有节点，且连线总长度最短的树。

### 1. Kruskal 算法

### 2. Prim 算法

## 最短路径

广度优先算法只能用于 无权重的图。

### 1. Bellman-Ford 算法
Bellman-Ford 算法: 边的权重可以为负值。 (可以用来求解差分约束系统)

**路径松弛性质**： 如果 $p=<v_0, v_1, ..., v_k>$ 是从源节点 $v_0$ 到节点$v_k$的一条最短路径，并且我们对$p$中的边进行松弛操作的次序为 $(v_0, v_1), (v_1, v_2), ..., (v_{k-1}, v_k)$，则 $v_k.d=(v_0到v_k最短路径权重)$

```
def belllman_ford(G, w, s):
    for each node in G:
        for each edge (u, v) in G.E:
            # 松弛操作
            if v.d > u.d + w(u, v):
                v.d = u.d + w(u, v)
                v.pred = u
    # 检查图中是否存在权重为负值的环路，存在则返回 False
    for each edge (u, v) in G.E:
        if v.d > u.d + w(u, v):
            return False
    return True

# 有向无环图 单源最短路径，证明参考 路径松弛性质
def DAG_shortest_paths(G, w, s):
    topologically sort the vertices of G
    initialize G
    for each vertex u, taken in topologically sorted order:
        for each vertex v in G.Adj[u]:
            RELAX(u, v, w)
            
```

### 2. Dijkstra 算法
Dijkstra 算法: 要求所有边的权重都为非负值。
```
def dijkstra(G, w, s):
    initialize G
    S = []
    Q = G.V  # 最小优先队列，关键值为d值
    while Q:
        u = extract_min(Q)
        S.append(u)
        for each vertex v in G.adj[u]:
            RELAX(u, v, w)
            
```

## 最大流

流网络 是一个有向图，图中每一条边有一个非负的容量值$c$。
流 是一个实值函数$f$，对于图中所有节点 $u, v$:
$0<=f(u,v)<=c(u,v)$。
流$f$的值是指从源节点流出的总流量减去流入源节点的总流量。

流量守恒性质：除源节点和汇点外，流入一个节点的总流量必须等于流出该节点的总流量。

### Ford-Fulkerson 方法
1. 残存网络： 给定流网络G和流量f，残存网络由那些仍有空间对流量进行调整的边构成。即流网络的一条边的容量减去该边上的流量，如果差值为正，则将该边置于残存网络中。
2. 增广路径： 是残存网络中一条从源节点到汇点的简单路径。
3. 切割：Ford-Fulkerson方法核心就是沿着增广路径重复增加路径上的流量，直到找到一个最大流为止。

**最大流最小切割定理**： 一个流是最大流当且仅当其残存网络不包含任何增广路径。

```
def ford_fulkerson(G, s, t):
    for each edge (u, v) in G.E:
        (u, v).f = 0
    while there exist a path p from s to t in the residual network:
        cf(p) = min(cf(u, v): (u, v) is in p)
        for each edge (u, v) in p:
            if (u, v) in G.E:
                (u, v).f = (u, v).f + cf(p)
            else:
                (v, u).f = (v, u).f - cf(p)
```

### 最大二分匹配
