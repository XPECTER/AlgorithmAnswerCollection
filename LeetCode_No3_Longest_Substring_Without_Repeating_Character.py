class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        answer = 0

        length = len(s)
        if length <= 1:
            return length

        while r != length:
            idx = s[l:r].find(s[r], l, r)

            if -1 != idx:
                answer = max(answer, r - l)
                l += idx + 1
                r += 1
            else:
                r += 1

        return max(answer, r - l)

s = Solution()
a = s.lengthOfLongestSubstring('abcabcbb')
print(a)