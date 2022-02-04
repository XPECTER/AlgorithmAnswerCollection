import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        length = len(nums)

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        nums = nums + nums[:left]
        idx = (bisect.bisect_left(nums[left:], target) + left) % length

        return idx if nums[idx] == target else -1

print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))