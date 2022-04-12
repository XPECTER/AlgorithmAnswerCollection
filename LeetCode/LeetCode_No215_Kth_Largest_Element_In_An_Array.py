# Runtime: 52 ms, faster than 99.37% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.8 MB, less than 99.94% of Python3 online submissions for Kth Largest Element in an Array.

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    # def findKthLargets(self, nums: List[int], k: int) -> int:
    #     h = []
    #
    #     for n in nums:
    #         heapq.heappush(h, (-n, n))
    #
    #     for i in range(1, k + 1):
    #         if i == k:
    #             return heapq.heappop(h)[1]
    #
    #         heapq.heappop(h)


print(Solution().findKthLargets([3, 2, 1, 5, 6, 4], 2))

