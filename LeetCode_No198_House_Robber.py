from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Limit Exceeded
        # answers = []
        #
        # def dp(money, idx):
        #     if idx >= len(nums):
        #         answers.append(money)
        #         return
        #
        #     for i in range(2):
        #         if i % 2:
        #             dp(money, idx + 1)
        #         else:
        #             dp(money + nums[idx], idx + 2)
        #
        # dp(0, 0)
        # return max(answers)

        # Runtime: 49 ms, faster than 34.02% of Python3 online submissions for House Robber.
        # Memory Usage: 13.9 MB, less than 83.51% of Python3 online submissions for House Robber.
        dp = [-1] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]

# print(Solution().rob([2, 7, 9, 3, 1]))
# print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([90, 0, 0, 95, 1, 1]))
# print(Solution().rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
