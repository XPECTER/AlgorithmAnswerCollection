def Solution(count, fear_lst):
    answer = 0
    fear_lst.sort()

    cnt = 0
    for i in range(len(fear_lst)):
        cnt += 1
        if cnt >= i:
            answer += 1
            cnt = 0

    return answer

print(Solution(5, [2, 3, 1, 2, 2]))
print(Solution(5, [3, 3, 2, 2, 1]))