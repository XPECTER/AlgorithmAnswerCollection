import sys


def budget_distribution(budget: list, total):
    budget.sort()
    avg = total // len(budget)

    if avg <= budget[0]:
        return total // len(budget)
    elif sum(budget) <= total:
        return budget[-1]

    prev_mid = 0
    mid = avg
    result = 0

    while prev_mid != mid:
        s = 0
        cnt = 0
        for b in budget:
            if b >= mid:
                s += mid
            else:
                s += b
                cnt += 1

        if s > total:
            mid -= (s - total) // len(budget)
        else:
            result = mid
            prev_mid = mid
            mid += (total - s) // (len(budget) - cnt)

    return result


input = sys.stdin.readline
n = int(input())
budget_lst = list(map(int, input().split()))
t = int(input())

print(budget_distribution(budget_lst, t))


# print(budget_distribution([120, 110, 140, 150], 443))
# print(budget_distribution([120, 110, 140, 150], 485))
# print(budget_distribution([70, 80, 30, 40, 100], 450))