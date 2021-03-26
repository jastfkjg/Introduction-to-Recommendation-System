"""
Segment Tree
"""

class SegmentTree:
    def __init__(self, nums):
        """
        tree 数组索引从1开始算起
        """
        self.n = len(nums)
        self.tree = [0 for _ in range(2*self.n)]
        for i in range(n, 2*n):
            tree[i] = nums[i-n]
        for i in range(n-1, 0, -1):
            tree[i] = self.merge(tree[2*i], tree[2*i+1])

    def merge(self, left, right):
        """
        根据情况选择merge函数，例：求区间和
        """
        return left + right 


    def update(self, i, val):
        i = i + self.n
        tree[i] = val 
        while i > 1:
            i = i // 2  #父节点
            tree[i] = self.merge(tree[2*i], tree[2*i+1])


    def query(self, left, right):
        """
        get the result from range [left, right], 例；求区间和
        """
        left += self.n
        right += self.n 
        res = 0
        while left < right:
            if left & 1 == 1:
                res += tree[left]
                left += 1

            if right & 1 == 1:
                right -= 1
                res += tree[right]

            left >>= 1
            right >>= 1

        return res 


        
