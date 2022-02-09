import sys
from collections import defaultdict, deque


input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
dist = [INF] * (n+1)
dist[1] = 0
q = deque([(0, 1)])
cnt = 0
while q:
    far, node = q.popleft()
    visited[node] = True
    cnt += 1

    for adj in graph[node]:
        if not visited[adj]:
            dist[adj] = min(dist[adj], far + 1)
            q.append((far + 1, adj))

result = max(dist[1:])
print(dist, cnt)
print(dist.index(result), result, dist.count(result))