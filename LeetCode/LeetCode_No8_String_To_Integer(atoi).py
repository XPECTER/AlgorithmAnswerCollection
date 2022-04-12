class Solution:
    def myAtoi(self, s: str) -> int:
        flag = False
        answer = [0, 0]
        sign = ''
        s = s.replace(' ', '')

        for i in range(len(s)):
            if s[i].isdigit() and flag == False:
                flag = True
                answer[0] = i

                if i != 0:
                    if s[i - 1] == '-' or s[i - 1] == '+':
                        sign = s[i - 1]

            if flag == True:
                if s[i].isalpha():
                    answer[1] = i
                    break
                elif i == len(s) - 1:
                    answer[1] = i + 1

        result = int(sign + s[answer[0]:answer[1]])

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31
        else:
            return result

a = Solution()
print(a.myAtoi('4193 with words'))
print(a.myAtoi('419'))