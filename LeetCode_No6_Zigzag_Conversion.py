# 문제 : 입력받은 문자열을 numRows만큼의 line으로 지그재그 표현하기
# ex:   PAYPALISHIRING =>
# P   A   H   N     1   5   9     13    17
# A P L S I I G     2 4 6 8 10 12 14 16 18 ......
# Y   I   R         3   7   11    15    19

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                    # 한 줄로 표현하는건 입력받은 문자열과 같다. 그냥 return
            return s

        l = len(s)
        cycle = (numRows - 1) * 2
        answer = []

        for i in range(numRows):
            for j in range(i, l, cycle):
                answer.append(s[j])

                # 첫 줄과 끝 줄이 아니고 길이를 넘어가지 않으면
                if i != 0 and i != numRows - 1 and j + cycle - 2 * i < l:
                    answer.append(s[j + cycle - 2 * i])

        return "".join(answer)


a = Solution()
print(a.convert("PAYPALISHIRING", 3))
# Output : PAHNAPLSIIGYIR