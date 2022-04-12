# import sys
# input = sys.stdin.readline
#
# house, hub = map(int, input().split())
# addr = []
# for _ in range(house):
#     addr.append(int(input()))
#
# addr.sort()
#
# if hub <= 2:
#     return addr[-1] - addr[0]

import bisect

def install_router(addr: list, router: int) -> int:
    addr.sort()

    if router <= 2:
        return addr[-1] - addr[0]

    # 라우터가 3개 이상일 때
    start = 1
    end = addr[-1] - addr[0]
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        count = 1
        pos = addr[0]

        for i in range(1, len(addr)):
            if addr[i] >= pos + mid:
                pos = addr[i]
                count += 1

        if count >= router:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer

print(install_router([1, 2, 8, 4, 9], 3))
print(install_router([1, 2, 8, 4, 9], 2))