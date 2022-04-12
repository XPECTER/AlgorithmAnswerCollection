import sys
import bisect


input = sys.stdin.readline
N, x = map(int, input().split())
lst = list(map(int, input().split()))

l = bisect.bisect_left(lst, x)
if not (0 <= l < len(lst)) or lst[l] != x:
    print(-1)
else:
    r = bisect.bisect_right(lst, x)
    print(r - l)
