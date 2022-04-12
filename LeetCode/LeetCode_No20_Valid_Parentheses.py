# Runtime: 32 ms, faster than 73.42% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.3 MB, less than 64.70% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opener = "({["
        pair = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in opener:
                stack.append(c)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if pair[c] != top:
                    return False

        return not stack


if __name__ == "__main__":
    a = Solution()
    assert a.isValid("{}{}{}{}")
