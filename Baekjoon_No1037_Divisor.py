# https://www.acmicpc.net/problem/1037

import sys

N = int(input())
a = sorted(map(int, sys.stdin.readline().split()))
print(a[0] * a[-1])

