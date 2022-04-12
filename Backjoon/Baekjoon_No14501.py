import sys
input = sys.stdin.readline

n = int(input())
benefits = []
for _ in range(n):
    benefits.append(tuple(map(int, input().split())))

print(benefits)
answers = []

def dp(day, pay):
    if day > n:
        return

    answers.append(pay)
    if day == n:
        return

    for i in range(2):
        if i % 2:
            dp(day + benefits[day][0], pay + benefits[day][1])
        else:
            dp(day + 1, pay)

dp(0, 0)
print(max(answers))