# 노드의 개수 : n
# 시작 노드 번호 : k
# 모든 노드의 최단거리를 구하고 그 중 가장 큰 값을 return
# 모든 노드의 최단거리를 구할 수 없다면 return -1
from typing import List
import heapq
INF = int(1e9)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        dist = [INF] * len(graph)

        for i in times:
            graph[i[0]].append((i[1], i[2]))

        q = [(0, k)]
        dist[k] = 0

        while q:
            acc, curr = heapq.heappop(q)

            if dist[curr] < acc:
                continue

            for adj, d in graph[curr]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))

        result = max(dist[1:])
        return result if result != INF else -1


assert Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
assert Solution().networkDelayTime([[1, 2, 1]], 2, 1) == 1
assert Solution().networkDelayTime([[1, 2, 1]], 2, 2) == -1
