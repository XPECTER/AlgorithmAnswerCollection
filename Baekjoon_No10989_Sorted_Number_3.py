import sys

input = sys.stdin.readline
print = sys.stdout.write

lst = [0]*10000
n = int(input())

for _ in range(n):
    lst[int(input()) - 1] += 1

for i in range(len(lst)):
    if lst[i]:
        while lst[i] > 1000:
            print((str(i+1) + '\n') * 1000)
            lst[i] -= 1000
        print((str(i + 1) + '\n') * lst[i])
