# Runtime: 121 ms, faster than 14.55% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 14.8 MB, less than 85.57% of Python3 online submissions for Design Circular Queue.
# Linked List Solution
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# class MyCircularQueue:
#     def __init__(self, k: int):
#         self.front = None
#         self.rear = None
#         self.max_element = k
#         self.count = 0
#
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#
#         if self.rear:  # head is not None
#             self.rear.next = Node(value, None)
#             self.rear = self.rear.next
#         else:
#             self.front = Node(value, None)
#             self.rear = self.front
#
#         self.count += 1
#         return True
#
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#
#         node = self.front
#         if self.front == self.rear:
#             self.front = self.front.next
#             self.rear = self.rear.next
#         else:
#             self.front = self.front.next
#
#         del node
#
#         self.count -= 1
#         return True
#
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#
#         return self.front.val
#
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#
#         return self.rear.val
#
#     def isEmpty(self) -> bool:
#         return True if not self.count else False
#
#     def isFull(self) -> bool:
#         return True if self.count == self.max_element else False


# Runtime: 68 ms, faster than 82.93% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 15.1 MB, less than 8.48% of Python3 online submissions for Design Circular Queue.
class MyCircularQueue:
    def __init__(self, k: int):
        self.front = 0          # 가장 앞의 인덱스
        self.rear = -1          # -1부터 시작해야 index에러가 안난다.
        self.max_size = k       # 사이즈를 가지고 있으면 return하기 쉬움. 대신 enq, deq에서 계산을 해야함
        self.size = 0
        self.array = [0] * k    # 데이터가 저장된 array

    # if success enQ, return true
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.max_size
        self.array[self.rear] = value
        self.size += 1
        return True

    # if success deQ, return true
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    # Front is None, return -1
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.array[self.front]

    # Rear is None, return -1
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.array[self.rear]

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.max_size else False


if __name__ == "__main__":
    # queue = MyCircularQueue(3)
    # print(queue.enQueue(1))
    # print(queue.enQueue(2))
    # print(queue.enQueue(3))
    # print(queue.enQueue(4))
    # print(queue.Rear())
    # print(queue.isFull())
    # print(queue.deQueue())
    # print(queue.enQueue(4))
    # print(queue.Rear())

    queue = MyCircularQueue(6)
    print(queue.enQueue(6))
    print(queue.Rear())
    print(queue.Rear())
    print(queue.deQueue())
    print(queue.enQueue(5))
    print(queue.Rear())
    print(queue.deQueue())
    print(queue.Front())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
