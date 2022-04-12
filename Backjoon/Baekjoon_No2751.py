import heapq
import sys

# # time : 2021ms, memory: 135652KB
# input = sys.stdin.readline
# a = []
# n = int(input())
# for _ in range(n):
#     heapq.heappush(a, int(input()))
#
# print("\n".join([str(heapq.heappop(a)) for _ in range(len(a))]))
#
#
# # time: 1156ms, memory: 155208KB
# input = sys.stdin.readline
# a = []
# n = int(input())
# for _ in range(n):
#     a.append(int(input()))
#
# print("\n".join(map(str, sorted(a))))

# time: 864ms, memory: 125444KB
input = sys.stdin.readline
a = [0] * 2000001
n = int(input())
for _ in range(n):
    a[int(input())] = 1

print("\n".join([str(i) for i in range(-1000000, 1000001, 1) if a[i]]))
