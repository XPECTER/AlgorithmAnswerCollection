import heapq
import sys

input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    x = int(input())
    if x == 0:
        print(0) if len(h) == 0 else print(heapq.heappop(h))
    else:
        heapq.heappush(h, x)
