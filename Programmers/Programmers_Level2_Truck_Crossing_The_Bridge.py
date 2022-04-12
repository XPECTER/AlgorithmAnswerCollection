# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


# 테스트 1 〉	통과 (0.61ms, 10.2MB)
# 테스트 2 〉	통과 (9.15ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (7.22ms, 10.2MB)
# 테스트 5 〉	통과 (79.33ms, 10.3MB)
# 테스트 6 〉	통과 (22.77ms, 10.3MB)
# 테스트 7 〉	통과 (0.99ms, 10.2MB)
# 테스트 8 〉	통과 (0.10ms, 10.2MB)
# 테스트 9 〉	통과 (2.71ms, 10.2MB)
# 테스트 10 〉	통과 (0.11ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.18ms, 10.2MB)
# 테스트 13 〉	통과 (1.23ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0

    while truck_weights or total_weight != 0:
        if truck_weights and total_weight + truck_weights[0] <= weight:
            q[0] = truck_weights.popleft()
            total_weight += q[0]

        total_weight -= q[-1]
        q[-1] = 0
        q.appendleft(q.pop())
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
