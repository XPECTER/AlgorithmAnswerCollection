import heapq


def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    cur_time = -1
    spent_time = 0
    tasks = []
    idx, now = 0, 0

    while idx < len(jobs):
        for j in jobs[idx:]:
            if cur_time < j[0] <= now:
                heapq.heappush(tasks, [j[1], j[0]])

        if tasks:
            t = heapq.heappop(tasks)
            cur_time = now
            now += t[0]
            spent_time += now - t[1]
            idx += 1
        else:
            now += 1

    return spent_time // len(jobs)


print(solution([[0, 3], [2, 6], [1, 9]])) # 9
print(solution([[0, 3], [1, 9], [2, 6]])) # 9
print(solution([[2, 9], [3, 6], [1, 3]])) # 9
print(solution([[10, 9], [3, 6], [0, 3]])) # 6
# print(solution([[0, 1], [0, 2], [0, 3], [0, 4]])) #
# print(solution([[0, 4], [0, 3], [0, 2], [0, 1]])) #
# print(solution([[1, 3], [1, 9], [2, 6]])) #
print(solution([[0, 5], [1, 2], [5, 5]])) #