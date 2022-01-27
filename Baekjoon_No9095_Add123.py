# to solve by DFS
# time : 72ms
# n = int(input())
# a = []
#
# for i in range(n):
#     cnt = 0
#     case = int(input())
#     answers = []
#
#     def dfs(elem, case: int) -> None:
#         if case == 0:                       # for로 갈 필요도 없이 바로 return
#             answers.append(list(elem))      # cnt라는 변수를 둬서 경우의 수만 저장해도 되지만, 일단 모든 방법을 다 저장
#             print(elem)
#             return
#
#         for i in range(1, 4):               # 1,2,3까지만 돈다.
#             if case - i >= 0:
#                 dfs(elem + [i], case - i)   # 더하는게 아닌 빼면서 진행한다. ex) 7을 입력받았을 때, 0에서 더하면서 7을 만드는게 아닌, 7에서 빼면서 진행
#             else:
#                 return  # 0보다 작은건 for를 돌 필요가 없다. 바로 return
#
#     dfs([], case)           # 빈 문자 리스트와 우리가 만들 수(ex) 7)를 넣는다.
#     print(len(answers))     # 모든 경우의 수가 다 들어있다.



# solve by DP
# time : 72 ms
n = int(input())

dp = [0] * 10
dp[0] = 1
dp[1] = 2
dp[2] = 4       # dp = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    case = int(input())
    if dp[case-1] != 0:      # memoization(여기 문제에선 케이스의 수를 입력받기 때문에 이미 계산한 값이 있다면 바로 print)
        print(dp[case-1])
        continue

    for j in range(3, case):
        if dp[j] == 0:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3] # 점화식

    print(dp[case-1])
