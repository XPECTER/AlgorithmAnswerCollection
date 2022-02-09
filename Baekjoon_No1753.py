from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

vertex, edge = map(int, input().split())
starting_point = int(input())
graph = defaultdict(list)
dist = [INF] * (vertex + 1)

for _ in range(edge):
    start, dest, cost = map(int, input().split())
    graph[start].append((dest, cost))

dist[starting_point] = 0
q = [(0, starting_point)]

while q:
    acc, s = heapq.heappop(q)

    if dist[s] < acc:
        continue

    for d, v in graph[s]:
        cost = acc + v
        if cost < dist[d]:
            dist[d] = cost
            heapq.heappush(q, (cost, d))

for i in range(1, vertex + 1):
    print(dist[i] if dist[i] != INF else 'INF')
