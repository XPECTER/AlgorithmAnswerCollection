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


result = 0
for i in range(int(input())):
    word = input()
    print(list(word), sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)