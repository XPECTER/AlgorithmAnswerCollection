from typing import List


# Runtime: 32 ms, faster than 73.39% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.3 MB, less than 33.10% of Python3 online submissions for Letter Combinations of a Phone Number.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        answer = []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def DFS(new_str: str) -> str:
            for char in mapping[digits[len(new_str)]]:
                make_str = new_str + char

                if len(make_str) == len(digits):
                    answer.append(make_str)
                else:
                    DFS(make_str)

            return

        DFS('')

        return answer


if __name__ == "__main__":
    # print(Solution().letterCombinations("23"))
    # print(Solution().letterCombinations(""))
    # print(Solution().letterCombinations("2"))
    print(Solution().letterCombinations("234"))
    print(Solution().letterCombinations("2943"))
    print(Solution().letterCombinations("2222"))
    print(Solution().letterCombinations("7979"))
