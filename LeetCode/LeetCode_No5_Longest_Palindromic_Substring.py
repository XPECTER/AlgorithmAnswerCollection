# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    # 첫번째 풀이
    # Runtime: 1221 ms, faster than 51.07% of Python3 online submissions for Longest Palindromic Substring.
    # Memory Usage: 14.5 MB, less than 35.37% of Python3 online submissions for Longest Palindromic Substring.
    def longestPalindrome(self, s: str) -> str:
        dict = {}
        answer = [0, 1]                     # 처음 생각한 내용은 index 하나만 사용해서 푸는 방법이었다.

        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]].append(i)        # 모든 문자의 index를 dict에 넣는다

                for j in dict[s[i]]:        # 해당 문자의 index를 전부 찾아가며 회문인지 판별한다.
                    sub = s[j:i+1]
                    if sub == sub[::-1]:                            # 회문(palindrom)이라면,
                        if (answer[1] - answer[0]) < (i - j + 1):   # 가장 긴 문자열인가?
                            answer = [j, i + 1]                     # 가장 긴 회문을 저장
                        break

            else:
                dict[s[i]] = [i]

        return s[answer[0]:answer[1]]       # 가장 긴 회문이 나오긴 한다. 하지만 속도가 느리다.

    # 두번째 풀이
    # Runtime: 299 ms, faster than 93.18% of Python3 online submissions for Longest Palindromic Substring.
    # Memory Usage: 14.3 MB, less than 81.37% of Python3 online submissions for Longest Palindromic Substring.
    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:     # 길이가 1이하인 문자는 그냥 return
            return s

        new_str = ""

        # 회문 판별 함수
        def extend(left: int, right: int) -> str:
            # two pointer로 하나씩 증감하면서 판별한다.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s) - 1):
            # 회문의 가장 짧은 예는 짝수 길이는 'bb', 홀수 길이는 'bab'
            # 가장 긴 문자열을 찾으면서 저장
            # extend(i, i+1)은 짝수길이 회문, (i, i+2)는 홀수길이 회문
            new_str = max(new_str, extend(i, i+1), extend(i, i+2), key=len)

        return new_str


a = Solution()
print(a.longestPalindrome2("aabbbbbbb"))
# Output : bbbbbbb