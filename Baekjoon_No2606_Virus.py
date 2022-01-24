import sys
from collections import defaultdict

N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

# print(graph)

stack = [1]
is_visit = [False] * (N+1)
cnt = -1

while stack:
    com = stack.pop()
    if is_visit[com]:
        continue

    is_visit[com] = True
    cnt += 1

    for i in graph[com]:
        if not is_visit[i]:
            stack.append(i)

print(cnt)
