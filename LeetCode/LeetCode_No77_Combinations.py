from typing import List

from itertools import combinations


class Solution:
    # Runtime: 123 ms, faster than 82.54% of Python3 online submissions for Combinations.
    # Memory Usage: 15.6 MB, less than 93.90% of Python3 online submissions for Combinations.
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(map(list, list(combinations([i for i in range(1, n+1)], k))))
        return list(map(list, list(combinations(range(1, n+1), k))))


    # Runtime: 704 ms, faster than 17.89% of Python3 online submissions for Combinations.
    # Memory Usage: 15.7 MB, less than 81.38% of Python3 online submissions for Combinations.
    def combine_DFS(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def DFS(elem: List, start: int, k: int) -> None:
            if 0 == k:
                answer.append(list(elem))
                return

            for i in range(start, n + 1):
                elem.append(i)
                DFS(elem, i + 1, k - 1)
                elem.pop()

            return

        DFS([], 1, k)

        return answer


if __name__ == "__main__":
    # print(Solution().combine(6, 4))
    print(Solution().combine_DFS(6, 3))
