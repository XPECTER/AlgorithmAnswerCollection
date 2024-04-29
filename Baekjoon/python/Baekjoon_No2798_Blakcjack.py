# brute force used for
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
card = sorted(map(int, input().split()))
answer = 0

for i in range(len(card) - 2):
    for j in range(i + 1,len(card) - 1):
        for k in range(j + 1, len(card)):
            s = card[i] + card[j] + card[k]
            if s > m:
                break
            else:
                answer = max(answer, s)

print(answer)

# brute force used recursive function
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
card = sorted(map(int, input().split()))
answer = 0

