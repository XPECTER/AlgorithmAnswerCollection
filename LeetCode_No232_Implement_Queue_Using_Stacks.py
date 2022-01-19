# Runtime: 41 ms, faster than 30.59% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 14.4 MB, less than 10.53% of Python3 online submissions for Implement Queue using Stacks.

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack1:
            self.stack1.append(x)
            return

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return

    def pop(self) -> int:
        if self.empty():
            return None

        return self.stack1.pop()

    def peek(self) -> int:
        return None if not self.stack1 else self.stack1[-1]

    def empty(self) -> bool:
        return True if not self.stack1 else False


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())