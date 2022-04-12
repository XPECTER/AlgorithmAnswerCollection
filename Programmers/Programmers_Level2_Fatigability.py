from itertools import permutations


# def solution(k, dungeons):
#     p = permutations(dungeons)
#     answer = 0
#
#     for case in p:
#         clear = 0
#         f = k
#
#         for dungeon in case:
#             if f >= dungeon[0]:
#                 f -= dungeon[1]
#                 clear += 1
#
#         answer = max(answer, clear)
#
#         if answer == len(dungeons):
#             return answer
#
#     return answer

answer = 0
N = 0
visit = []

def dfs(k, cnt, dungeons):
    global answer

    for i in range(N):
        if k >= dungeons[i][0] and not visit[i]:
            visit[i] = 1
            dfs(k, cnt+1, dungeons)
            visit[i] = 0

    return

def solution(k, dungeons):
    global answer, N, visit
    N = len(dungeons)
    visit = [0] * N
    dfs(k, 0, dungeons)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
