# 前缀树 Trie

前缀树是N叉树的一种，用来存储字符串，树中每个节点代表一个字符串。叶子节点代表的字符串是由节点本身的原始字符串以及通往该叶子节点路径上所有的字符组成。

前缀树的重要特性：节点的所有后代都与该节点相关的字符串有着共同的前缀。

注： 前缀树的根节点表示 空字符串。

如何表示前缀树：

1. 数组：用大小为26的数组来存储子节点。用x-'a'作为索引查找数组中相应的子节点。 但可能导致空间的浪费。
2. Map：每个节点声明一个HashMap，键是字符，值是对应的子节点。

```
class TrieNode:
    def __init__(self, c):
        self.c = c
        self.isWord = False
        self.children = {}

root = TrieNode("")
```

### 插入操作
```
def insert(root, s):
    for c in s:
        if c not in root.children:
            root.children[c] = new TrieNode(c)

        root = root.children[c]
    root.isWord = True
```

### 搜索操作
```
def search(root, s):
    for c in s:
        if c not in root.children:
            return False
        root = root.children[c]
    return root.isWord

def startsWith(root, prefix):
    for c in prefix:
        if c not in root.children:
            return False
        root = root.children[c]
    return True

```

## 线段树

线段树是一棵平衡二叉树，根节点代表整个区间的和。线段树的每个节点都对应一个区间，但不保证所有的区间都是线段树的节点。

如果节点n对应存储区间[l,r]的和，那它的左右子节点分别存储[l, (l+r)//2], [(l+r)//2+1, r]的和。

### 构建线段树
```
def build(nums, l, r, p):
    if l == r:
        tree[p] = nums[l]
    else:
        mid = (l + r) // 2
        build(nums, l, mid, 2*p)
        build(nums, mid+1, r, 2*p+1)
        tree[p] = tree[2*p] + tree[2*p+1]
```