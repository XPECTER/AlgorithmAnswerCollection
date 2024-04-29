def solution():
    n = int(input())
    answer = 0

    while n % 5:
        n -= 3
        answer += 1
    
    return answer + n // 5 if n >= 0 else -1

print(solution())