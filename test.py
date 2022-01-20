# a = [1,2,3,4]
#
# print(id(a))
#
#
# b = [1,2,3,4]
#
# # if a is b:
# #     print(True)
# # else:
# #     print(False)
# #
# # if a == b:
# #     print(True)
# # else:
# #     print(False)
#
# print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))
#
# a[0] = [1,2,3]
#
# print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))
#
# print(a)
#
# a[0] = 1
#
# print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))
#
# a[0] += 3
#
# print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))

# n = 6
# strs = ['(())())', '(((()())()', '(()())((()))', '((()()(()))(((())))()', '()()()()(()()())()', '(()((())()(']
#
# for i in range(int(n)):
#     # str = input()
#     str = strs[i]
#     stack = []
#     for c in str:
#         if c == "(":
#             stack.append(c)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 print("NO")
#                 break
#     else:
#         if not stack:
#             print("YES")
#         else:
#             print("NO")
#

# stack = [4, 3, 7, 2, 1]
# per = [8, 6, 5, 1, 2, 7, 3, 4]


# from collections import deque
#
# test_case = input()
#
# # sys.stdin.readline() << 오
#
# for _ in range(int(test_case)):
#     amount_doc, target = map(int, input().split())
#     importance = deque([(idx, val) for idx, val in enumerate([x for x in map(int, input().split())])])
#     print(importance)
#
#     if amount_doc == 1:
#         print(1)
#         continue
#
#     cnt = 1
#     while True:
#         m_p = max(importance, key=lambda x: (x[1]))
#         print(m_p)
#
#         while importance[0] != m_p:
#             importance.append(importance.popleft())
#             print(importance)
#
#         if importance[0][0] == target:
#             print(cnt)
#             break
#         else:
#             importance.popleft()
#             cnt += 1

    # importance.append(importance.popleft())
    # importance.append(importance.popleft())
    #
    # m_p = max(importance, key=lambda x: (x[1]))
    # print(m_p)


def solution(mylist):
    answer = [[0 for i in range(len(mylist))] for i in range(len(mylist))]

    for i in range(len(mylist)):
        for j in range(len(mylist)):
            answer[i][j] = mylist[j][i]

    return answer


solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])