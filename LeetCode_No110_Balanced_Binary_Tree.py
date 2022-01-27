# Runtime: 48 ms, faster than 88.92% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19 MB, less than 49.24% of Python3 online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0

            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(root) != -1