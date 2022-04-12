# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# Runtime: 239 ms, faster than 75.34% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 16.6 MB, less than 14.20% of Python3 online submissions for Insertion Sort List.
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        cur = dummy = ListNode()

        while head:
            while cur.next and cur.next.val < head.val:             # head가 가리키는 노드가 들어갈 자리를 찾는 부분
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next   # 각 노드마다 다시 연결하기

            if head and head.val < cur.val:                         # 최적화 부분. 헤드의 값이 더 크면 굳이 되돌아갈 필요가 없다
                cur = dummy

        return dummy.next                                           # 우리가 필요한건 노드의 다음 부분부터


# assert Solution().insertionSortList([4, 2, 1, 3]) == [1, 2, 3, 4]
# assert Solution().insertionSortList([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]