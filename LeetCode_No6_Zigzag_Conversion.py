# https://leetcode.com/problems/zigzag-conversion/

# ex:   PAYPALISHIRING =>
# P   A   H   N     1   5   9     13    17
# A P L S I I G     2 4 6 8 10 12 14 16 18 ......
# Y   I   R         3   7   11    15    19

# 다른 사람의 풀이
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:                    # 한 줄로 표현하는건 입력받은 문자열과 같다. 그냥 return
#             return s
#
#         l = len(s)
#         cycle = (numRows - 1) * 2
#         answer = []
#
#         for i in range(numRows):
#             for j in range(i, l, cycle):
#                 answer.append(s[j])
#
#                 # 첫 줄과 끝 줄이 아니고 길이를 넘어가지 않으면
#                 if i != 0 and i != numRows - 1 and j + cycle - 2 * i < l:
#                     answer.append(s[j + cycle - 2 * i])
#
#         return "".join(answer)


# Runtime: 105 ms, faster than 23.91% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14.5 MB, less than 25.37% of Python3 online submissions for Zigzag Conversion.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dict = {}
        answer = ""

        if numRows == 1:
            return s

        for i in range(numRows):
            dict[i] = []

        carry = 1
        idx = 0

        for j in range(len(s)):
            dict[idx].append(s[j])
            idx += carry

            if idx == 0 or idx == numRows - 1:
                carry *= -1

        for k in range(numRows):
            answer += "".join(dict[k])

        return answer


a = Solution()
print(a.convert("PAYPALISHIRING", 3))
# Output : PAHNAPLSIIGYIR