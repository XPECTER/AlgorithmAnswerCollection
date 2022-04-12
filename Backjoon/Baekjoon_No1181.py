# 내장함수 sort 사용
# time : 92 ms
# import sys
#
# n = int(sys.stdin.readline())
# lst = set()
#
# for _ in range(n):
#     word = sys.stdin.readline().rstrip('\n')
#     lst.add(word)
#
# lst = sorted(lst)     # ['but', 'cannot', 'hesitate', 'i', 'im', 'it'....]
# lst.sort(key=len)     # ['i', 'im', 'it', 'but', ...]
#
# print("\n".join(lst))


# 문제풀이 전용 mergesort 구현
# time : 320 ms
import sys

n = int(sys.stdin.readline())
lst = set()

for _ in range(n):
    word = sys.stdin.readline().rstrip('\n')
    lst.add(word)

lst = list(lst)

def word_merge(L: list, R: list):
    i = j = 0
    result = []

    while i < len(L) and j < len(R):
        if len(L[i]) < len(R[j]):
            result.append(L[i])
            i += 1
        elif len(L[i]) == len(R[j]):
            for char_idx in range(len(L[i])):
                if L[i][char_idx] == R[j][char_idx]:
                    continue
                elif L[i][char_idx] > R[j][char_idx]:
                    result.append(R[j])
                    j += 1
                    break
                else:
                    result.append(L[i])
                    i += 1
                    break
        else:
            result.append(R[j])
            j += 1

    if i < len(L):
        result.extend(L[i:])

    if j < len(R):
        result.extend(R[j:])

    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    return word_merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


print("\n".join(merge_sort(lst)))
