"""
disjoint-set:
    1. make_set(x): 建立一个新的集合，唯一元素是x
    2. union(x, y): 将包含x和y的两个集合合并成一个集合
    3. find_set(x): 返回一个包含x的集合的指针
"""
class disjointSet:
    def __init__(self, connected):
        self.nums = len(connected)
        self.parent = list(range(self.nums))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = find(parent[i])
        
        return self.parent[i]

    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)

    def disjointNum(self):
        return sum(parent[i] == i for i in range(self.nums))
