import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lo = 0
hi = len(lst)

while lo < hi:
    mid = lo + ((hi - lo) // 2)

    if lst[mid] < mid:
        lo = mid + 1
    else:
        hi = mid

if 0 <= lo < len(lst) and lst[mid] == mid:
    print(mid)
else:
    print(-1)