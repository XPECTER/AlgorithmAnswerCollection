import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []
answer = []

for i in range(n):
    x = int(input())

    if i % 2:
        heapq.heappush(min_heap, x)
    else:
        heapq.heappush(max_heap, -x)

    if min_heap and -max_heap[0] > min_heap[0]:
        mx = -heapq.heappop(max_heap)
        mn = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -mn)
        heapq.heappush(min_heap, mx)

    answer.append(-max_heap[0])

print("\n".join(map(str, answer)))