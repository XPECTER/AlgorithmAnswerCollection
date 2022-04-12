# to solve by combinations
# time : 68 ms

from itertools import combinations, product
import sys

L, C = map(int, sys.stdin.readline().split())
v = {'a', 'e', 'i', 'o', 'u'}   # 필터. 입력받은 문자가 모음이면 모음 List로 들어간다. 5개밖에 안되서 list를 써도 될듯?
con = []        # 자음 List
vow = []        # 모음 List
answer = []     # 완성된 암호 List

for c in sys.stdin.readline().split():
    if c in v:
        vow.append(c)   # 모음이면 vow에 append하고,
    else:
        con.append(c)   # 자음이면 con에 append한다.

cnt = 1     # 모음이 1개일때 부터 while 진입
while cnt <= len(vow) and L - cnt >= 2:         # 모음은 1개 이상, 자음은 2개 이상 있어야 한다.
    ex_c = list(map("".join, list(combinations(con, L - cnt))))     # 자음이 L-1개, L-2개...의 조합을 구한다
    ex_v = list(map("".join, list(combinations(vow, cnt))))         # 모음이 1개, 2개... 의 조합을 구한다.
    answer.extend(list(map("".join, list(product(ex_v, ex_c)))))    # 위의 조합 2개를 합친다.
    cnt += 1    # 모음의 개수를 1개 늘려서 더 구한다.
    # print(ex_c, ex_v, answer)

for word in sorted(list(map("".join, (map(sorted, answer))))):      # 모든 원소마다 정렬하고(aswi -> aisw), 전체적으로 한 번 더 정렬한다.([acit ,aisw])
    print(word)


# to solve by backtracking
# time : 84 ms
# import sys
#
# vowels = {'a', 'e', 'i', 'o', 'u'}                          # dfs에서 모음인지 체크하기 위해 선언
# L, C = map(int, sys.stdin.readline().split())               # L, C 입력받음
# chars = [c for c in sorted(sys.stdin.readline().split())]   # 입력받은 문자를 정렬해서 List화
# # print(chars) # a t c i s w -> ['a', 'c', 'i', 's', 't', 'w']
# answer = []
#
#
# def dfs(strs: list, start: int, cnt: int) -> None:      # strs : 재귀하면서 만들어가는 문자열, cnt : 모음의 개수
#     if cnt > L - 2 or start > len(chars):                                     # 최소한 자음 2개는 포함되어야 한다.
#         return
#
#     if len(strs) == L and cnt >= 1:                     # start는 시작할 index
#         answer.append("".join(strs))
#         return
#
#     for i in range(start, len(chars)):
#         if chars[i] in vowels:
#             dfs(strs + [chars[i]], i + 1, cnt + 1)
#         else:
#             dfs(strs + [chars[i]], i + 1, cnt)
#
#     return
#
#
# dfs([], 0, 0)
#
# for word in answer:
#     print(word)



