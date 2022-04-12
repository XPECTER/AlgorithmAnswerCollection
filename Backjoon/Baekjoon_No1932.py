import sys
import copy
input = sys.stdin.readline

n = int(input())
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))
#
# answer = copy.deepcopy(t)
# answer = []
#
# for i in range(n - 1):
#     for j in range(len(t[i])):
#         answer[i + 1][j] = max(answer[i + 1][j], answer[i][j] + t[i + 1][j])
#         answer[i + 1][j + 1] = max(answer[i + 1][j + 1], answer[i][j] + t[i + 1][j + 1])
#
# print(max(answer[-1]))

answer = []

for i in range(n):
    f = t[i]
    answer = [max(a+c, b+c) for a, b, c in zip([0]+answer, answer+[0], f)]

print(max(answer))

# [0, 7] [7, 0] [3, 8]
# a = 0 b = 7 c = 3 max(3, 10)
# a = 7 b = 0 c = 8 max(15, 8)
# [10, 15]
