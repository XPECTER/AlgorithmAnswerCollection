from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(dict)

        for a, b, p in flights:
            graph[a][b] = p

        q = [(0, src, K + 1)]

        while q:
            price, node, k = heapq.heappop(q)

            if node == dst:
                return price

            if k > 0:
                for j in graph[node]:
                    heapq.heappush(q, (price + graph[node][j], j, k - 1))

        return -1


print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
