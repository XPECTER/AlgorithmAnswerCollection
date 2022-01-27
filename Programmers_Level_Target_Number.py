def solution(numbers, target):
    answer = []

    def dfs(start, acc):
        if start == len(numbers):
            if acc == target:
                answer.append(acc)
            return

        dfs(start + 1, acc + numbers[start])
        dfs(start + 1, acc - numbers[start])

        return

    dfs(0, 0)
    return len(answer)


# print(solution([1, 1, 1, 1, 1], 3)) #return 5
assert solution([1, 1, 1, 1, 1], 3) == 5

# 수정 후
# 테스트 1 〉	통과 (356.41ms, 10.2MB)
# 테스트 2 〉	통과 (362.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.37ms, 10.2MB)
# 테스트 4 〉	통과 (1.37ms, 10.2MB)
# 테스트 5 〉	통과 (10.51ms, 10.1MB)
# 테스트 6 〉	통과 (0.67ms, 10.2MB)
# 테스트 7 〉	통과 (0.35ms, 10.2MB)
# 테스트 8 〉	통과 (2.90ms, 10.2MB)