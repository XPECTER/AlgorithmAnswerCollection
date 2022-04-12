from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Runtime: 343 ms, faster than 8.46% of Python3 online submissions for Search a 2D Matrix II.
        # Memory Usage: 20.3 MB, less than 97.85% of Python3 online submissions for Search a 2D Matrix II.
        col = bisect.bisect_left(matrix[0], target)
        if col < len(matrix[0]) and matrix[0][col] == target:
            return True

        for i in range(col):
            lst = list(map(lambda x: x[i], matrix))
            f = bisect.bisect_left(lst, target)
            if f < len(lst) and lst[f] == target:
                return True

        return False

        #
        # if not matrix:
        #     return False
        #
        # row = 0
        # col = len(matrix[0]) - 1
        #
        # while col >= 0 and row < len(matrix):
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] > target:
        #         col -= 1
        #     elif matrix[row][col] < target:
        #         row += 1
        #
        # return False

        # Runtime: 160 ms, faster than 91.50% of Python3 online submissions for Search a 2D Matrix II.
        # Memory Usage: 20.3 MB, less than 97.85% of Python3 online submissions for Search a 2D Matrix II.
        # return any(target in row for row in matrix)


# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(Solution().searchMatrix([[-1, 3]], 3))


