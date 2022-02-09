# from itertools import combinations, product
# import sys
#
#
# # L, C = map(int, sys.stdin.readline().split())
# L, C = 4, 6
# v = {'a', 'e', 'i', 'o', 'u'}   # 필터. 입력받은 문자가 모음이면 모음 List로 들어간다. 5개밖에 안되서 list를 써도 될듯?
# con = []        # 자음 List
# vow = []        # 모음 List
# answer = []     # 완성된 암호 List
#
#
# l = ['a', 'c', 's', 'i', 't', 'w']
# # for c in sys.stdin.readline().split():    # 백준에서 입력받기 위함
# for c in l:                                 # 임시로 배열을 만듦
#     if c in v:
#         vow.append(c)   # 모음이면 vow에 append하고,
#     else:
#         con.append(c)   # 자음이면 con에 append한다.
#
# cnt = 1     # 모음이 1개일때 부터 while 진입
# while cnt <= len(vow) and L - cnt >= 2:         # 모음은 1개 이상, 자음은 2개 이상 있어야 한다.
#     ex_c = list(map("".join, list(combinations(con, L - cnt))))     # 자음이 L-1개, L-2개...의 조합을 구한다
#     ex_v = list(map("".join, list(combinations(vow, cnt))))         # 모음이 1개, 2개... 의 조합을 구한다.
#     answer.extend(list(map("".join, list(product(ex_v, ex_c)))))    # product는 두 리스트의 조합이다. 위의 조합 2개를 조합한다.
#     cnt += 1    # 모음의 개수를 1개 늘려서 더 구한다.
#     print("자음 조합 : ", ex_c)
#     print("모음 조합 : ", ex_v)
#     print("모음이 %d개 일 때 조합 : " % (cnt - 1), list(map("".join, list(product(ex_v, ex_c)))))
#     print("------------------------------------------------")
#
# print("모든 조합 : ", answer)
# print("정렬 후 하나씩 출력")
# for word in sorted(list(map("".join, (map(sorted, answer))))):      # 모든 원소마다 정렬하고(aswi -> aisw), 전체적으로 한 번 더 정렬한다.([acit ,aisw])
#     print(word)


import sys


def getMaxAllocation(requests, N, budget):
    sortedRequests = sorted(requests)
    n = N
    for i in range(N):
        avg = budget // n
        print(avg)
        if sortedRequests[i] > avg:
            return avg
        budget -= sortedRequests[i]
        n -= 1
    return sortedRequests[N-1]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    requests = list(map(int, sys.stdin.readline().split()))
    budget = int(sys.stdin.readline())
    print(getMaxAllocation(requests, N, budget))