from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 30 ms, faster than 90.76% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.6 MB, less than 46.99% of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None      # 헤드를 하나씩 옮기면서 헤드에 있던 노드를 rev로 연결한다.

        while head:
            rev, rev.next, head = head, rev, head.next

        return rev


if __name__ == "__main__":
    a = Solution()

    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    head = a.reverseList(n1)

    while head:
        print(head.val)
        head = head.next

