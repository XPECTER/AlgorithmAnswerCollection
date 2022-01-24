# to solve by DFS
# time : 72ms
n = int(input())
a = []

for i in range(n):
    cnt = 0
    case = int(input())
    answers = []

    def dfs(elem, case: int) -> None:
        if case == 0:
            answers.append(list(elem))
            return

        for i in range(1, 4):
            if case - i >= 0:
                dfs(elem + [i], case - i)
            else:
                return

    dfs([], case)
    print(len(answers))



# solve by DP
# time : 72 ms
# n = int(input())

# dp = [0] * 10
# dp[0] = 1
# dp[1] = 2
# dp[2] = 4
#
# for j in range(3, 10):
#     if dp[j] == 0:
#         dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]
#
# print(dp)

# for i in range(n):
#     case = int(input())
#
#     for j in range(3, case):
#         if dp[j] == 0:
#             dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
#
#     print(dp[case-1])
