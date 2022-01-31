# Runtime: 156 ms, faster than 98.63% of Python3 online submissions for Sort List.
# Memory Usage: 30 MB, less than 97.43% of Python3 online submissions for Sort List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        node = head
        while node:
            lst.append(node.val)
            node = node.next

        lst.sort()
        node = head
        for i in range(len(lst)):
            node.val = lst[i]
            node = node.next

        return head