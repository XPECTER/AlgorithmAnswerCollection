# https://leetcode.com/problems/number-of-islands/
# Runtime: 323 ms, faster than 68.29% of Python3 online submissions for Number of Islands.
# Memory Usage: 17 MB, less than 39.82% of Python3 online submissions for Number of Islands.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        is_visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        answer = 0

        def dfs(i, j, grid):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                if not is_visit[i][j]:
                    is_visit[i][j] = 1

                    dfs(i + 1, j, grid)
                    dfs(i, j + 1, grid)
                    dfs(i - 1, j, grid)
                    dfs(i, j - 1, grid)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not is_visit[i][j] and grid[i][j] == "1":
                    dfs(i, j, grid)
                    answer += 1

        return answer


if __name__ == "__main__":
    print(Solution().numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))

    print(Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))


