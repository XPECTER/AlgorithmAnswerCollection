# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# Runtime: 285 ms, faster than 30.81% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 18.7 MB, less than 94.10% of Python3 online submissions for Serialize and Deserialize Binary Tree.
class Codec:
    def serialize(self, root):
        if not root:
            return ''

        serial = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            serial.append(str(node.val)) if node else serial.append('#')

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ' '.join(serial)

    def deserialize(self, data):
        if len(data) == 0:
            return []

        values = data.split()
        root = TreeNode(values[0])
        queue = collections.deque([(root)])
        idx = 1
        while queue:
            node = queue.popleft()

            if values[idx] != "#":
                node.left = TreeNode(int(values[idx]))
                queue.append(node.left)
            idx += 1

            if values[idx] != "#":
                node.right = TreeNode(int(values[idx]))
                queue.append(node.right)
            idx += 1
        return root


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

n6 = TreeNode(-6)
n7 = TreeNode(7)
n2 = TreeNode(0)
n4 = TreeNode(4, n6, n7)
n5 = TreeNode(5)
n3 = TreeNode(1)
n1 = TreeNode(-1, n2, n3)

print(ser.serialize(n1))
print(deser.deserialize('-1 0 1 # # # #'))

# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]

# ans = deser.deserialize(ser.serialize(root))