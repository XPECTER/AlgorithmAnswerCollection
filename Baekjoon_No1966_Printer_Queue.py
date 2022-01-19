# https://www.acmicpc.net/problem/1966
# time : 96 ms

from collections import deque
import sys

test_case = input()

for _ in range(int(test_case)):
    amount_doc, target = map(int, sys.stdin.readline().split())
    importance = deque([(idx, val) for idx, val in enumerate([x for x in map(int, sys.stdin.readline().split())])])

    if amount_doc == 1:
        print(1)
        continue

    cnt = 1
    while True:
        m_p = max(importance, key=lambda x: (x[1]))

        while importance[0] != m_p:
            importance.append(importance.popleft())

        if importance[0][0] == target:
            print(cnt)
            break
        else:
            importance.popleft()
            cnt += 1

# input :
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

# output :
# 1
# 2
# 5