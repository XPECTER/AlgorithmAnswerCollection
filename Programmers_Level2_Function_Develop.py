import math
from collections import deque


# 첫 풀이
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.30ms, 10.1MB)
# 테스트 3 〉	통과 (0.68ms, 10.2MB)
# 테스트 4 〉	통과 (0.15ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.37ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.27ms, 10.2MB)
# 테스트 10 〉	통과 (0.52ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
def solution(progresses, speeds):
    answer = []
    progress = 0
    task = 0

    while progress != len(progresses):
        if progresses[progress] >= 100:
            progress += 1
            task += 1
            continue

        if task != 0:
            answer.append(task)
            task = 0

        for i in range(progress, len(progresses)):
            progresses[i] += speeds[i]

    answer.append(task)
    return answer


# 승수님 생각에 의한 풀이
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
def solution2(progresses, speeds):
    answer = []
    leng = len(progresses)
    prog_day = deque([100] * leng)
    for i in range(leng):
        prog_day[i] = math.ceil((prog_day[i] - progresses[i]) / speeds[i])

    while prog_day:
        val = prog_day.popleft()
        cnt = 1

        while prog_day and val >= prog_day[0]:
            prog_day.popleft()
            cnt += 1

        answer.append(cnt)
    return answer


# print(solution2([93, 30, 55], [1, 30, 5]))
print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
