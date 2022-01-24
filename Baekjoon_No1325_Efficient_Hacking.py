import sys
from collections import deque, defaultdict


N, M = map(int, sys.stdin.readline().split())
dic = defaultdict(list)

for _ in range(M):
    val, key = map(int, sys.stdin.readline().split())
    dic[key].append(val)

answer = []
queue = deque()
max_cnt = 0

for i in range(1, N + 1):
    cnt = 0
    is_visit = set([i])
    queue.append(i)

    while queue:
        idx = queue.popleft()
        cnt += 1

        for adj in dic[idx]:
            if adj not in is_visit:
                is_visit.add(adj)
                queue.append(adj)

    if max_cnt < cnt:
        answer.clear()
        answer.append(i)
        max_cnt = cnt
    elif max_cnt == cnt:
        answer.append(i)

print(*answer)


