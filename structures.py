class MaxHeap:
    def __init__(self):
        self.item = [None]
        self.len = 0

    def __len__(self):
        return len(self.item) - 1

    def __str__(self):
        return str(self.__class__) + str(self.item[1:])

    def _percolate_up(self) -> None:
        cur = len(self)
        parents = cur // 2

        while parents > 0:
            if self.item[parents] < self.item[cur]:
                self.item[parents], self.item[cur] = self.item[cur], self.item[parents]

            cur = parents
            parents = cur // 2

        return

    def _percolate_down(self, cur) -> None:
        biggest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.item[left] > self.item[biggest]:
            biggest = left

        if right <= len(self) and self.item[right] > self.item[biggest]:
            biggest = right

        if biggest != cur:
            self.item[cur], self.item[biggest] = self.item[biggest], self.item[cur]
            self._percolate_down(biggest)

        return

    def insert(self, val: int) -> bool:
        self.item.append(val)
        self._percolate_up()
        return True

    def extract(self) -> int:
        if len(self) < 1:
            return -1

        result = self.item[1]
        self.item[1] = self.item[-1]
        self.item.pop()
        self._percolate_down(1)

        return result


def test_maxheap_we_made(lst, k):
    maxheap = MaxHeap()

    for i in lst:
        maxheap.insert(i)

    print(maxheap)
    return [maxheap.extract() for _ in range(k)][-1]


assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6


# import heapq
# # h = heapq()
# h = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# heapq.heapify(h) # 최소힙
# print(h)

# max heap을 min heap처럼 쓰려면 데이터를 넣을 때 음수로 넣으면 된다.
# nums = [4, 1, 7, 3, 8, 5]
# heap = []
#
# for num in nums:
#   heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
#
# while heap:
#   print(heapq.heappop(heap)[1])  # index 1


