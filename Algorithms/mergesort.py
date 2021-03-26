"""
mergsort
"""
def merge(A, p, q, r):
    # n1 = p - q + 1
    # n2 = r - q 
    left = A[p:q+1]
    right = A[q+1:r+1]
    # 加入哨兵牌
    left.append(float("inf"))
    right.append(float("inf"))

    i, j = 0, 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) //  2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge_sort_with_index(nums, left, right):
    index = [i for i in range(len(nums))]
    if left < right:
        mid = (left + right) // 2
        merge_sort_with_index(nums, left, mid)
        merge_sort_with_index(nums, mid+1, right)
        merge_with_index(nums, left, mid, right, index)

def merge_with_index(nums, left, mid, right, index):
    i, j = left, mid+1
    tmp = []
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            # res[index[i]] += j - mid - 1
            tmp.append(nums[i])
            i += 1
        elif nums[i] > nums[j]:
            tmp.append(nums[j])
            j += 1

    while i <= mid:
        tmp.append(nums[i])
        i += 1
    
    while j <= right:
        tmp.append(nums[j])
        j += 1

    for m in range(len(tmp)):
        index[left+m] = tmp[m]

        

"""
链表归并排序
"""
class LinkListMergeSort:
    @staticmethod
    def sortLinkList(head):
        # 结束条件
        if head == None or head.next == None:
            return head 

        midNode = middleNode(head)
        rightHead = midNode.next
        # 切断
        midNode.next = None

        left = sortLinkList(head)
        right = sortLinkList(rightHead)

    @staticmethod
    def middleNode(head):
        if not head or not head.next:
            return head
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def merge(head1, head2):
        dummyHead = ListNode(0)
        tmp = dummyHead 

        while head1 and head2:
            if head1.val <= head2.val:
                tmp.next = head1
                head1 = head1.next
            else:
                tmp.next = head2
                head2 = head2.next
            tmp = tmp.next

        tmp.next = head1 if head1 != None else head2
        return dummyHead.next



if __name__ == "__main__":
    A = [2, 3, 5, 1, 7, 3, 9, 4, 2, 8, 5]
    print("input: ", A)
    merge_sort(A, 0, len(A)-1)
    print("merge sort: ", A)
