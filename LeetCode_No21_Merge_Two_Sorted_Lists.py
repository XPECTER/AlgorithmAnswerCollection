class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


a_e1 = ListNode(4)
a_e2 = ListNode(2, a_e1)
a_e3 = ListNode(1, a_e2)

b_e1 = ListNode(4)
b_e2 = ListNode(3, b_e1)
b_e3 = ListNode(1, b_e2)

answer = Solution()
l = answer.mergeTwoLists(a_e3, b_e3)

while l != None:
    print(l.val)
    l = l.next