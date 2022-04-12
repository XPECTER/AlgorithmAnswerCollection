# Runtime: 129 ms, faster than 28.05% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 15.5 MB, less than 29.60% of Python3 online submissions for Merge Two Binary Trees.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion
        # if root1 and root2:
        #     new_node = TreeNode(root1.val + root2.val)
        #     new_node.left = self.mergeTrees(root1.left, root2.left)
        #     new_node.right = self.mergeTrees(root1.right, root2.right)
        #
        #     return new_node
        # else:
        #     return root1 or root2

        # BFS
        stack = [(root1, root2)]

        while stack:
            n1, n2 = stack.pop()

            if not n1 or not n2:
                continue

            n1.val += n2.val

            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))

            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))

        return root1 if root1 else root2