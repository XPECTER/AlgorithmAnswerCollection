from typing import List

# Runtime: 28 ms, faster than 99.20% of Python3 online submissions for Largest Number.
# Memory Usage: 13.9 MB, less than 99.00% of Python3 online submissions for Largest Number.
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(lambda x: x*10,map(str, nums)), reverse=True)
        return str(int("".join(map(lambda x: x[:int(len(x)/10)], nums))))

#
# # lst = ["333", "303030", "343434", "555", "999"]
# # lst = ["999999991", "9"]
# lst = ["0", "0"]
#
# lst = sorted(map(lambda x: x*10, map(str, lst)), reverse=True)
# lst = list(map(lambda x: x[:int(len(x)/10)], lst))
# print(str(int("".join(lst))))
