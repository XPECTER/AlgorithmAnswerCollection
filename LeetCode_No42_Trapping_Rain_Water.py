#Runtime: 76 ms, faster than 70.53% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 15.9 MB, less than 12.78% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: list) -> int:
        water = 0
        left, right = 0, len(height) - 1                        # two pointers를 사용한 풀이
        left_max, right_max = height[left], height[right]       # 가장 긴 막대를 지정해서 사이의 물을 계산할 것이다.

        while left < right:                                     # 두 포인터가 겹치면 종료(한 칸씩만 이동할 것이기 때문)
            left_max = max(left_max, height[left])              # 왼쪽의 가장 높은 막대
            right_max = max(right_max, height[right])           # 오른쪽의 가장 높은 막대

            if left_max <= right_max:                           # 둘 중 큰 막대를 기준으로 다가 갈 것이다
                water += left_max - height[left]                # 가장 높은 왼쪽 막대에서 현재 막대를 뺀 만큼 물을 더해준다.
                left += 1                                       # 포인터 옮기고(왼쪽은 +)
            else:
                water += right_max - height[right]              # 가장 높은 오른쪽 막대에서
                right -= 1                                      # 포인터 옮기고(오른쪽은 -)

        return water                                            # 다 더한 물의 양을 return


if __name__ == "__main__":
    a = Solution()
    print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(a.trap([10, 0, 2, 3, 4, 6, 7, 1, 2, 3, 9]))