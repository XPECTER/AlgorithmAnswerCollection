from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        #         left = 0
        #         right = len(numbers) - 1

        #         while left < right:
        #             if numbers[left] + numbers[right] > target:
        #                 right -= 1
        #             elif numbers[left] + numbers[right] < target:
        #                 left += 1
        #             else:
        #                 return [left + 1, right + 1]

        # bisect
        for i, v in enumerate(numbers):
            candidate = target - v
            k = bisect.bisect_left(numbers, candidate, i + 1)
            if k < len(numbers) and numbers[k] == candidate:
                return [i + 1, k + 1]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([0, 0, 1, 2], 0))