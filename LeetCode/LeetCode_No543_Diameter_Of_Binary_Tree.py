from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 48 ms, faster than 59.06% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.4 MB, less than 53.39% of Python3 online submissions for Diameter of Binary Tree.
class Solution:
    def __init__(self):
        self.long = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.long = max(self.long, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.long


if __name__ == "__main__":
    a = TreeNode(15)
    b = TreeNode(7)
    c = TreeNode(20, a, b)
    d = TreeNode(9)
    e = TreeNode(3, d, c)

    a2 = TreeNode(2)
    b2 = TreeNode(1, None, a2)

    print(Solution().diameterOfBinaryTree(e))