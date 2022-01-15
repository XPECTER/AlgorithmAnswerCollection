# from typing import Optional

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n1_idx = n2_idx = 0
        n1_len = len(nums1)
        n2_len = len(nums2)
        s_l = []

        while n1_idx != n1_len or n2_idx != n2_len:
            if n1_idx == n1_len:
                s_l.append(nums2[n2_idx])
                n2_idx += 1
                continue
            elif n2_idx == n2_len:
                s_l.append(nums1[n1_idx])
                n1_idx += 1
                continue

            if nums1[n1_idx] >= nums2[n2_idx]:
                s_l.append(nums2[n2_idx])
                n2_idx += 1
            else:
                s_l.append(nums1[n1_idx])
                n1_idx += 1

        print(s_l)

        if len(s_l) % 2:
            print(s_l[int(len(s_l) / 2)])
            return s_l[int(len(s_l) / 2)]
        else:
            print(s_l[int(len(s_l) / 2) - 1], s_l[int(len(s_l) / 2)])
            return float((s_l[int(len(s_l) / 2) - 1] + s_l[int(len(s_l) / 2)]) / 2)


a = Solution()
print(a.findMedianSortedArrays([1, 2], [3, 4]))