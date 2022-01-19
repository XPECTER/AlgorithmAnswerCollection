# https://www.acmicpc.net/problem/1920
# ex)
# input :
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

import sys

N = input()                                                 # 자연수 N
A = [i for i in map(int, sys.stdin.readline().split())]     # N개의 정수 A[1] ... A[N]
M = input()                                                 # 찾고 싶은 번호의 개수 M
B = [i for i in map(int, sys.stdin.readline().split())]

dic = {}
for i in A:
    dic[i] = 0

for i in B:
    sys.stdout.write("1\n" if i in dic else "0\n")
