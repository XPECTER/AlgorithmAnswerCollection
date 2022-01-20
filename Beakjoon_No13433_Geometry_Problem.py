# https://www.acmicpc.net/problem/13433

from typing import List


def calc_min(n: int, radiuses: List) -> float:
    answer = 0

    for i in range(n - 1):
        answer += ((radiuses[i+1]+radiuses[i])**2 - (radiuses[i+1]-radiuses[i])**2)**0.5

    return answer


if __name__ == "__main__":
    print(calc_min(2, [1, 2]))
    print(calc_min(3, [7, 7, 7]))
    print(calc_min(3, [20, 10, 30]))
    # print(calc_min(5, [100, 100, 11, 11, 25]))

    # ri, rj 사이의 거리보다 