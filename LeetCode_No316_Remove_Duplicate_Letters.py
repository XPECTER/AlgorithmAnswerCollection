from collections import Counter


# Runtime: 40 ms, faster than 61.51% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 14.3 MB, less than 49.48% of Python3 online submissions for Remove Duplicate Letters.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, stack = Counter(s), []

        for c in s:
            count[c] -= 1

            if c in stack:
                continue

            while stack and c < stack[-1] and count[stack[-1]] > 0:
                stack.pop()

            stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().removeDuplicateLetters("bcabc"))
    print(Solution().removeDuplicateLetters("cbacdcbc"))
