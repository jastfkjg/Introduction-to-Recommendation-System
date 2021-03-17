# 树

## 树的遍历

1. 前序
2. 中序
3. 后序
4. 逐层
   
序指的是根节点的位置顺序。

前序：先根节点，再左节点，再右节点。
中序：先左节点，再根节点，再右节点。
后序：先左节点，再右节点，再根节点。

<div align="center">
<img src="images/tree_dfs.jpg" width = "500">
</div>

### 前序遍历：

1. 递归 
```
res = []
def preorder(root):
    if not root: return
    res.append(root.value)
    preorder(root.left)
    preorder(root.right)

```

2. 迭代

```
def preorder(root):
    if not root: return
    res = []
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.value)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res
```

```
def preorder(root):
    if not root: return
    res, stack = [], []
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.value)
        # 先推入右节点
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
```

### 中序遍历

```
# 迭代
def inorder(root):
    if not root: return 
    res, stack = [], []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        res.append(node.value)
        node = stack.pop().right
    return res
```

### 后序遍历

```
# 迭代 v1
def postorder(root):
    if not root: return 
    res, stack = [], []
    stack.append(root)
    node = root
    while stack:
        # 栈顶非父节点，而是其右节点
        if stack[-1].right != node and stack[-1].left != node:
            gotoLeftMostLeaf()
        node = stack.pop()
        res.append(node.value)
    return res

def gotoLeftMostLeaf(stack):
    node = stack[-1]
    while node:
        if node.left:
            if node.right:
                stack.append(node.right)
            stack.append(node.left)
        else:
            stack.append(node.right)
        node = stack[-1]
    stack.pop() #去除最后一个空节点
```

```
# 迭代 v2: 后序遍历为前序遍历右子树的倒序
def postorder(root):
    res, stack = [], []
    node = root
    while node or stack:
        while node:
            res.append(node.value)
            stack.append(node)
            node = node.right
        node = stack.pop().left
    
    return res[::-1]
```

### 逐层遍历
-- 广度优先搜索 bfs (Queue)
```
def levelOrder(root) -> List[List[int]]:
        if not root: return []
        res, queue = [], [root]
        while queue:
                res_lever = []
                for i in range(len(queue)):
                    cur_node = queue.pop(0)
                    res_lever.append(cur_node.val)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
                res.append(res_lever)
        return res
```

## 常见问题

### 路径总和

### 构造树
- 根据 前序+中序 构造二叉树
- 根据 后序+中序 构造二叉树


### 最近公共祖先

```
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if(root==p||root==q||root==null) return root;

    TreeNode left=lowestCommonAncestor(root.left, p, q);
    TreeNode right=lowestCommonAncestor(root.right, p, q);

    if(left==null&&right==null) return null;
    if(left!=null&&right!=null) return root;
    
    return left==null ? right:left;
}
```
