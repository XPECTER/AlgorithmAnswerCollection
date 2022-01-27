# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime: 43 ms, faster than 33.10% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14.2 MB, less than 74.64% of Python3 online submissions for Invert Binary Tree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root