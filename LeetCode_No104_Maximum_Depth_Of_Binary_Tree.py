# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 48 ms, faster than 44.22% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.4 MB, less than 88.57% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])
        answer = 0

        while q:
            answer += 1

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return answer


if __name__ == "__main__":
    a = TreeNode(15)
    b = TreeNode(7)
    c = TreeNode(20, a, b)
    d = TreeNode(9)
    e = TreeNode(3, d, c)

    a2 = TreeNode(2)
    b2 = TreeNode(1, None, a2)

    print(Solution().maxDepth(b2))