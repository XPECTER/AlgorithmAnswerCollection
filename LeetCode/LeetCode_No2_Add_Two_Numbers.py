# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Runtime: 60 ms, faster than 96.21% of Python3 online submissions for Add Two Numbers.
    # Memory Usage: 14.4 MB, less than 45.08% of Python3 online submissions for Add Two Numbers.
    def addTwoNumbers(self, l1, l2):
        carry = 0

        # head와 lastNode에 빈 node를 넣는다.
        # tail뒤에 바로 새 노드를 붙이기 위해서 사용했다.
        head = tail = ListNode()

        while l1 or l2 or carry:
            if l1:                          # 정확히는 None이 아니면
                carry += l1.val
                l1 = l1.next                # l1 한 칸 이동
            if l2:
                carry += l2.val
                l2 = l2.next                # l2 한 칸 이동

            carry, n = divmod(carry, 10)    # carry는 10을 넘어갈 때 다음 수에 +1을 해주기 위해 사용
            newNode = ListNode(n)           # 10으로 나눈 나머지만 넣는다
            tail.next = newNode             # 포인터를 연결하고
            tail = newNode                  # tail은 새 노드를 가르키게 한다.

        return head.next                    # head는 빈 노드고 다음 노드부터가 데이터가 들어있다.