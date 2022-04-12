def solution(n: int, times: list):
    times.sort()

    lo = 0
    hi = times[-1] * (n-1)

    while lo < hi:
        mid = lo + ((hi - lo) // 2)
        s = 0

        for i in range(len(times)):
            s += mid // times[i]

        if s >= n:
            hi = mid
        else:
            lo = mid+1

    return lo


print(solution(6, [7, 10]))
print(solution(12, [3, 5, 7]))
print(solution(20, [2, 5, 10]))