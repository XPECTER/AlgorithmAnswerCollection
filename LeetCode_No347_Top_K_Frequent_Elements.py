# https://leetcode.com/problems/top-k-frequent-elements/

# Runtime: 92 ms, faster than 97.24% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.8 MB, less than 40.02% of Python3 online submissions for Top K Frequent Elements.

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]


if __name__ == "__main__":
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))