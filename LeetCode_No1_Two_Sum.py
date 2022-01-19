# https://leetcode.com/problems/two-sum/

class Solution:
    # Runtime: 62 ms, faster than 56.65% of Python3 online submissions for Two Sum.
    # Memory Usage: 15.7 MB, less than 8.50% of Python3 online submissions for Two Sum.
    def twoSum(self, nums: list, target: int) -> list:
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]    # i를 필요로 하는 인덱스와 같이 return한다.
            else:
                dic[target - nums[i]] = i   # 타겟에서 뺀 수를 키, 인덱스를 값으로 보관한다. 맞는 키가 들어오면 인덱스만 가져갈 수 있게

        # 문제 조건에 답이 한 가지는 반드시 존재한다고 한다.
        return [-1,-1]

a = Solution()
print(a.twoSum([2,7,9,11], 9))