# backtracking

回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就 “回溯” 返回，尝试别的路径。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为 “回溯点”。

## 模板
```
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }
    for (选择：树中子节点）) {
        处理节点;
        backtracking(路径，选择列表); 
        回溯，撤销处理结果;
    }
}
```

## 八皇后
```
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        res = []
        def solve(cur, matrix):
            # 找到解法
            if cur == n:
                ans = []
                for i in range(n):
                    line = ""
                    for j in range(n):
                        if matrix[i][j] != 'Q':
                            line += "."
                        else:
                            line += "Q"
                    ans.append(line)
                
                import copy
                res.append(copy.deepcopy(ans))
                return

            for i in range(n):
                if matrix[cur][i] == 0:
                    # 设置下游禁区 += 1
                    matrix[cur][i] = "Q"
                    for j in range(cur+1, n):
                        matrix[j][i] += 1
                        r = i + j - cur 
                        l = i - j + cur 
                        if r < n:
                            matrix[j][r] += 1
                        if l >= 0:
                            matrix[j][l] += 1
                    
                    # 子问题
                    solve(cur+1, matrix)

                    # 还原设置 -= 1
                    matrix[cur][i] = 0
                    for j in range(cur+1, n):
                        matrix[j][i] -= 1
                        r = i + j - cur 
                        l = i - j + cur 
                        if r < n:
                            matrix[j][r] -= 1
                        if l >= 0:
                            matrix[j][l] -= 1
        solve(0, matrix)
        return res 
```

