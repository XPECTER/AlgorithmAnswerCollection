# Runtime: 28 ms, faster than 85.56% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 14.3 MB, less than 44.63% of Python3 online submissions for Implement Queue using Stacks.

class Node:
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext


class MyQueue:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x, None)
            return

        node = self.head
        while node.pNext:
            node = node.pNext

        node.pNext = Node(x, None)
        return

    def pop(self) -> int:
        if not self.head:
            return None

        node = self.head
        self.head = self.head.pNext

        return node.val

    def peek(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return not self.head


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())