import sys

case = int(input())

for cnt in range(case):
    v1, v2 = (map(int, sys.stdin.readline().split()))

    v1 = min(v2-v1, v1)
    n = 1
    d = 1
    for i in range(1, v1 + 1):
        d *= i
        n *= v2+1-i

    print(n // d)