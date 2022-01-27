# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 372 ms, faster than 86.82% of Python3 online submissions for Longest Univalue Path.
# Memory Usage: 18 MB, less than 66.76% of Python3 online submissions for Longest Univalue Path.
class Solution:
    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, value) -> int:
            if node is None:
                return 0

            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)

            self.longest = max(self.longest, left + right)

            if node.val == value:
                return max(left, right) + 1
            else:
                return 0

        dfs(root, None)

        return self.longest

    # 책에 있는 풀이
    # result: int = 0
    #
    # def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    #     def dfs(node: TreeNode):
    #         if node is None:
    #             return 0
    #
    #         left = dfs(node.left)
    #         right = dfs(node.right)
    #
    #         if node.left and node.left.val == node.val:
    #             left += 1
    #         else:
    #             left = 0
    #
    #         if node.right and node.right.val == node.val:
    #             right += 1
    #         else:
    #             right = 0
    #
    #         self.result = max(self.result, left + right)
    #         return max(left, right)
    #
    #     dfs(root)
    #     return self.result

if __name__ == "__main__":
    a1 = TreeNode(1)
    b1 = TreeNode(1)
    c1 = TreeNode(4, a1, b1)
    f1 = TreeNode(5)
    d1 = TreeNode(5, None, f1)
    e1 = TreeNode(5, c1, d1)

    a2 = TreeNode(4)
    b2 = TreeNode(4)
    c2 = TreeNode(4, a2, b2)
    f2 = TreeNode(5)
    d2 = TreeNode(5, None, f2)
    e2 = TreeNode(1, c2, d2)

    print(Solution().longestUnivaluePath(e1))
    print(Solution().longestUnivaluePath(e2))
