# https://leetcode.com/problems/jewels-and-stones/
# input : jewels = "aA", stones = "aAAbbbb"
# output : 3

from collections import Counter

class Solution:
    # Runtime: 46 ms, faster than 23.31% of Python3 online submissions for Jewels and Stones.
    # Memory Usage: 14.3 MB, less than 45.55% of Python3 online submissions for Jewels and Stones.
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     count = Counter(stones)
    #     answer = 0
    #
    #     for char in jewels:
    #         answer += count[char]
    #
    #     return answer


    # Runtime: 50 ms, faster than 17.36% of Python3 online submissions for Jewels and Stones.
    # Memory Usage: 14.4 MB, less than 12.52% of Python3 online submissions for Jewels and Stones.
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)



if __name__ == "__main__":
    print(Solution().numJewelsInStones("aA", "aAAbbbb"))