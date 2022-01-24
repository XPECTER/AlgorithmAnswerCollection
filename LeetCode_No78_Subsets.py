from typing import List


# Runtime: 40 ms, faster than 45.09% of Python3 online submissions for Subsets.
# Memory Usage: 14.5 MB, less than 52.31% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def DFS(elem: List[int], start: int) -> None:
            answer.append(list(elem))

            for i in range(start, len(nums)):
                DFS(elem + [nums[i]], i + 1)
            return

        DFS([], 0)

        return answer


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
