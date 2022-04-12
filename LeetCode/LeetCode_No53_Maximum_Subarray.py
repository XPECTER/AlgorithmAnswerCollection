from typing import List

# kadane algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # concise way
        # for i in range(1, len(nums)):
        #     nums[i] = max(nums[i], nums[i - 1] + nums[i])
        # return max(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)