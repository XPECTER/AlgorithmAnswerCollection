# https://leetcode.com/problems/median-of-two-sorted-arrays/


# Runtime: 144 ms, faster than 24.46% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.4 MB, less than 93.68% of Python3 online submissions for Median of Two Sorted Arrays.
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         n1_idx = n2_idx = 0
#         n1_len = len(nums1)
#         n2_len = len(nums2)
#         s_l = []
#
#         while n1_idx != n1_len or n2_idx != n2_len:
#             if n1_idx == n1_len:
#                 s_l.append(nums2[n2_idx])
#                 n2_idx += 1
#                 continue
#             elif n2_idx == n2_len:
#                 s_l.append(nums1[n1_idx])
#                 n1_idx += 1
#                 continue
#
#             if nums1[n1_idx] >= nums2[n2_idx]:
#                 s_l.append(nums2[n2_idx])
#                 n2_idx += 1
#             else:
#                 s_l.append(nums1[n1_idx])
#                 n1_idx += 1
#
#         print(s_l)
#
#         if len(s_l) % 2:
#             print(s_l[int(len(s_l) / 2)])
#             return s_l[int(len(s_l) / 2)]
#         else:
#             print(s_l[int(len(s_l) / 2) - 1], s_l[int(len(s_l) / 2)])
#             return float((s_l[int(len(s_l) / 2) - 1] + s_l[int(len(s_l) / 2)]) / 2)


# from typing import List
#
#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l = sorted(nums1 + nums2)
#         length = len(l)
#
#         if len(l) % 2:
#             return float(l[int(length / 2)])
#         else:
#             return (float(l[int(length / 2)]) + float(l[int(length / 2) - 1])) / 2


# 이분 탐색 풀이법
import sys
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2) : return self.findMedianSortedArrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = -sys.maxsize if partitionX == 0 else nums1[partitionX - 1]
            minRightX = sys.maxsize if partitionX == x else nums1[partitionX]

            maxLeftY = -sys.maxsize if partitionY == 0 else nums2[partitionY - 1]
            minRightY = sys.maxsize if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                return max(maxLeftX, maxLeftY) if (x + y) % 2 != 0 else (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1


a = Solution()
print(a.findMedianSortedArrays([1, 2], [3, 4]))