# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Runtime: 54 ms, faster than 84.48% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 54.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
# two points solution

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = 0
#         r = 1
#         answer = 0
#
#         length = len(s)
#         if length <= 1:
#             return length
#
#         while r != length:
#             idx = s[l:r].find(s[r], l, r)
#
#             if -1 != idx:
#                 answer = max(answer, r - l)
#                 l += idx + 1
#                 r += 1
#             else:
#                 r += 1
#
#         return max(answer, r - l)


# Runtime: 49 ms, faster than 94.20% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 24.75% of Python3 online submissions for Longest Substring Without Repeating Characters.
# dictionary solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        answer = 0
        start = 0

        for i in range(len(s)):
            if s[i] in pos and pos[s[i]] >= start:
                answer = max(answer, i - start)
                start = pos[s[i]] + 1

            pos[s[i]] = i

        return max(answer, len(s[start:]))


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))      # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))         # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))        # 3
    print(Solution().lengthOfLongestSubstring(" "))             # 1
    print(Solution().lengthOfLongestSubstring(""))              # 0
    print(Solution().lengthOfLongestSubstring("aab"))           # 2
    print(Solution().lengthOfLongestSubstring("cdd"))           # 2
    print(Solution().lengthOfLongestSubstring("abcdefg"))       # 7
    print(Solution().lengthOfLongestSubstring("abba"))          # 2
    print(Solution().lengthOfLongestSubstring("dvdf"))          # 3
