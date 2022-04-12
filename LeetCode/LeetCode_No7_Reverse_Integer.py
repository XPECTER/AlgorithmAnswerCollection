# https://leetcode.com/problems/reverse-integer/

#Runtime: 58 ms, faster than 5.85% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.1 MB, less than 74.45% of Python3 online submissions for Reverse Integer.
#풀이 시간 : 7분 40초

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        val = int(str(x)[::-1]) if sign == 1 else sign * int(str(x)[::-1][:-1])
        return val if val < 2**31-1 and val > -2**31 else 0