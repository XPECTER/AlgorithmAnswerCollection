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


# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# nodes = [[] for i in range(N)]
#
# for idx, val in enumerate(map(int, input().split())):
#     if val == -1: continue
#     nodes[val] += [idx]
#
# print(nodes)
# r = int(input())
#
# def remove(rem):
#     for i in nodes[rem]:
#         remove(i)
#     nodes[rem] = None
#
# remove(r)
#
# print(nodes)
# print(sum([1 if i in ([], [r]) else 0 for i in nodes]))

# lst = [1 if [i] in ([1,3], [0,2]) else 0 for i in range(5)]
# print(lst)

# if [] in [[], [1, 2]]:
#     print(True)
# else:
#     print(False)

# A = int(input())
# B = int(input())
# answer = [str(A*B)]
# while B > 0:
#     answer.append(str((B % 10) * A))
#     B //= 10
# print("\n".join(answer[1:]+answer[:1]))


# A = int(input())
# if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
#     print(1)
# else:
#     print(0)


# h, m = map(int, input().split())
# if m >= 45:
#     print(f'{h} {m-45}')
# else:
#     h = h-1 if h > 0 else 23
#     m = m+15 if m < 45 else m+15-60
#     print(f'{h} {m}')


# import sys
# from collections import defaultdict
# case = int(input())
# answer = 0
#
# def check_word(word: str) -> bool:
#     if len(word) <= 1:
#         return True
#
#     dic = defaultdict(list)
#
#     for i in range(len(word)):
#         dic[word[i]].append(i)
#
#         if len(dic[word[i]]) <= 1 or i-1 in dic[word[i]]:
#             continue
#         else:
#             return False
#
#     return True
#
# for i in range(case):
#     word = sys.stdin.readline().rstrip('\n')
#     if check_word(word):
#         answer += 1
#
# print(answer)
#
#

# # print("".join(sorted(input(), reverse=True)))
# print(*sorted(input())[::-1], sep='')

# import sys
#
# lst = sys.stdin.readlines()[1:]
# lst.sort(key=lambda x: (int(x.split()[0]), int(x.split()[1])))
# sys.stdout.write("".join(lst))

# s = {1, 7, 5, 4}
# s = sorted(s)
# print(s)

lst = [[1, 4], [4, 5]]
# temp_lst = []
# temp_lst.append([lst[0][0], lst[1][1]])
# print(temp_lst)

print(lst)