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

stack = [4, 3, 7, 2, 1]
per = [8, 6, 5, 1, 2, 7, 3, 4]