"""
quicksort
"""
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    # choose pivot
    x = A[r] 
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

"""
k-th smallest
"""
def findKthSmallest(A, p, r, k):
    if r - p + 1 >= k:
        q = partition(A, p, r)
        if q-p+1 == k:
            return A[p:q+1]
        elif q-p+1 > k:
            return findKthSmallest(A, p, q-1, k)
        elif q-p+1 < k:
            return findKthSmallest(A, q+1, r, k-(q-p+1)) 

if __name__ == "__main__":
    A = [2, 3, 4, 5, 2, 4, 7, 3, 9, 0, 4, 7]
    print("input: ", A)
    quicksort(A, 0, len(A)-1)
    print("quicksort: ", A)
    kthSmallest = findKthSmallest(A, 0, len(A)-1, 5)
    print("5 smallest element: ", kthSmallest)

