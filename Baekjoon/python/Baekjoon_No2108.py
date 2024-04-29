# N은 홀수
# 1 <= N <= 500000
# -4000 <= x <= 4000

import sys
from collections import defaultdict, Counter

input = sys.stdin.readline
# print = sys.stdout.write
# dic = defaultdict(int)
lst = []
sum = 0
mn = 4001
mx = -4001

N = int(input())
for _ in range(N):
    x = int(input())
    # dic[x] += 1
    lst.append(x)
    sum += x
    mn = min(mn, x)
    mx = max(mx ,x)

lst.sort()
# average
avg = sum / N
if avg < 0:
    avg = -int(abs(avg) + 0.5)
else:
    avg = int(avg + 0.5)
print(avg)

# 중앙값
print(lst[len(lst)//2])

# 최빈값

# 범위
print(mx - mn)