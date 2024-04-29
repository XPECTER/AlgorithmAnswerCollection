import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    H, W, N = map(int, input().split())

    if N % H == 0:
        print(str(H) + str(-(-N // H))) if (-(-N // H)) >= 10 else print(str(H) + '0' + str(-(-N // H)))
    else:
        print(str(N % H) + str(-(-N // H))) if (-(-N // H)) >= 10 else print(str(N % H) + '0' + str(-(-N // H)))

