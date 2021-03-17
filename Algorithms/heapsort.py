
"""
heapsort
"""
def max_heapify(A, i):
    l = i * 2 + 1
    r = i * 2 + 2
    if l < len(A) and A[l] > A[i]:
        index = l
    else:
        index = i
    if r < len(A) and A[r] > A[index]:
        index = r
    if index != i:
        A[i], A[index] = A[index], A[i]
        max_heapify(A, index)

def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i)

def heapsort(A):
    build_max_heap(A)
    res = []
    for i in range(len(A)-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        res.append(A.pop())
        max_heapify(A, 0)
    return res

"""
Priority Queue:
    1. insert(A, x)
    2. maximum(A)
    3. extract_max(A)
    4. increase_key(A, x, k)

"""
import math
def maximum(A):
    return A[0]

def extract_max(A):
    if len(A) > 0:
        A[0], A[len(A)-1] = A[len(A)-1], A[0]
        ans = A.pop()
        max_heapify(A, 0)
        return ans

def increase_key(A, i, k):
    if A[i] > k:
        raise InvalidArgumentError
    A[i] = k
    while i > 0 and A[math.ceil(i/2)-1] < A[i]:
        A[i], A[math.ceil(i/2)-1] = A[math.ceil(i/2)-1], A[i]
        i = math.ceil(i/2) - 1

def insert(A, k):
    A.append(-float("inf"))
    increase_key(A, len(A)-1, k)


if __name__ == "__main__":
    A = [2, 4, 1, 6, 7, 3, 4, 2, 9, 10, 4, 5]
    print("input: ", A)
    build_max_heap(A)
    print("build max heap: ", A)
    res = heapsort(A)
    print("heapsort: ", res)
