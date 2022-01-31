import sys
input = sys.stdin.readline

def solution(X):
    # X = int(input())
    n = 1

    while n * (n + 1) // 2 < X:
        n += 1

    x = n*(n+1)//2 - X

    if n % 2 == 1:
        print(f'{x+1}/{n-x}')
    else:
        print(f'{n-x}/{x+1}')

# solution(1)
# solution(2)
# solution(3)
# solution(4)
# solution(5)
# solution(6)
# solution(7)
# solution(8)
# solution(9)
# solution(14)
