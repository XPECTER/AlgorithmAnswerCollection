from collections import defaultdict
import sys
input = sys.stdin.readline
INF = int(1e9)

cities = int(input())
buses = int(input())
graph = defaultdict(list)

for _ in range(buses):
    src, dst, cost = map(int, input().split())
    graph[src].append((dst, cost))

dist = [[INF] * (cities + 1) for _ in range(cities + 1)]
for i in range(1, cities + 1):
    dist[i][i] = 0

for key, val in graph.items():
    for d, c in val:
        if c < dist[key][d]:
            dist[key][d] = c

for k in range(1, cities + 1):
    for i in range(1, cities + 1):
        for j in range(1, cities + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, cities + 1):
    for j in range(1, cities + 1):
        if dist[i][j] == INF:
            dist[i][j] = 0

for i in range(1, cities + 1):
    print(*dist[i][1:])
