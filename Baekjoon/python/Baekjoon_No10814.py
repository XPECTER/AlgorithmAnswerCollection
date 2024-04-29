import sys

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    age, name = input().rstrip().split()
    lst.append((int(age), name))        # int로 안바꿔주면 사전 순 비교를 해버린다

lst.sort(key=lambda x: x[0])
for elem in lst:
    print(f'{elem[0]} {elem[1]}')


# 6
# 100 Yong
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung
# 19 Kong
# 35 Jung
