from typing import List

# Runtime: 252 ms, faster than 15.14% of Python3 online submissions for Merge Intervals.
# Memory Usage: 18.1 MB, less than 46.43% of Python3 online submissions for Merge Intervals.
# 일반 while문
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         idx = 0
#         result = []
#         intervals.sort(key=lambda x: x[0])
#
#         while idx < len(intervals) - 1:
#             sub = intervals[idx]
#             while idx < len(intervals) - 1 and sub[1] >= intervals[idx+1][0]:
#                 sub[1] = max(sub[1], intervals[idx+1][1])
#                 idx += 1
#
#             result.append(sub)
#             idx += 1
#
#         if idx < len(intervals):
#             result.append(intervals[idx])
#
#         return result


# print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))    # == [[1, 6], [8, 10], [15, 18]]
# print(Solution().merge([[1, 4], [4, 5]]))                       # == [[1, 5]]
# print(Solution().merge([[1, 4], [2, 3]]))                       # == [[1, 4]]

# Runtime: 211 ms, faster than 28.49% of Python3 online submissions for Merge Intervals.
# Memory Usage: 18.1 MB, less than 33.83% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if result and result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result += i,

        return result


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))    # == [[1, 6], [8, 10], [15, 18]]
print(Solution().merge([[1, 4], [4, 5]]))                       # == [[1, 5]]
print(Solution().merge([[1, 4], [2, 3]]))                       # == [[1, 4]]