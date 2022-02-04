from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
#         set1 = set(nums1)
#         set2 = set(nums2)

#         if len(set1) > len(set2):
#             return [x for x in set2 if x in set1]
#         else:
#             return [x for x in set1 if x in set2]


assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
assert Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or [9, 4]
