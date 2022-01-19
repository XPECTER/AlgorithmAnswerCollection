# https://www.acmicpc.net/problem/2164
# time : 260 ms

from collections import deque

amount_card = input()
q = deque([x + 1 for x in range(int(amount_card))])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])

# input : 6
# output : 4