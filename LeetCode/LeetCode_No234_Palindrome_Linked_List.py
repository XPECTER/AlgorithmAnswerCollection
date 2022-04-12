from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 844 ms, faster than 54.98% of Python3 online submissions for Palindrome Linked List.
    # Memory Usage: 47.1 MB, less than 50.89% of Python3 online submissions for Palindrome Linked List.
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        answer = deque()                                    # deque로 최적화

        while head:
            answer.append(head.val)                         # head의 내용을 deque로
            head = head.next

        while len(answer) > 1:                              # 뽑다보면 가운데 하나는 확인할 필요 없음(홀수개일때)
            if deque.popleft(answer) != deque.pop(answer):  # 양쪽에서 하나씩 뽑아 확인
                return False

        return True


    # Runtime: 713 ms, faster than 94.76% of Python3 online submissions for Palindrome Linked List.
    # Memory Usage: 31.3 MB, less than 99.70% of Python3 online submissions for Palindrome Linked List.
    def isPalindromeRunner(self, head: Optional[ListNode]) -> bool:
        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next

        return not rev


if __name__ == "__main__":
    a = Solution()

    n4 = ListNode(1)
    n3 = ListNode(2, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    print(a.isPalindromeRunner(n1))
    # print(a.isPalindromeRunner([1, 2, 2, 1]))