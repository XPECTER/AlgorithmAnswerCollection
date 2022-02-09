from collections import defaultdict, deque
import sys
input = sys.stdin.readline
INF = int(1e9)

students, cmp = map(int, input().split())
rank = [[INF] * (students+1) for _ in range(students+1)]
graph = defaultdict(list)
for _ in range(cmp):
    i, j = map(int, input().split())
    graph[i].append(j)

for i in range(students + 1):
    rank[i][i] = 0

for key, val in graph.items():
    for c in val:
        rank[key][c] = 1

answer = 0

for k in range(1, students + 1):
    for i in range(1, students + 1):
        for j in range(1, students + 1):
            rank[i][j] = min(rank[i][j], rank[i][k] + rank[k][j])

for i in range(1, len(rank)):
    print(*rank[i][1:])

for curr in range(students + 1):
    cnt = 0

    for node in range(students + 1):
        if rank[curr][node] != INF or rank[node][curr] != INF:
            cnt += 1

    if cnt == students:
        answer += 1

print(answer)