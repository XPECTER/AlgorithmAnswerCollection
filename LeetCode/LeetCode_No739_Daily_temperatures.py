from typing import List

# Runtime: 1192 ms, faster than 91.78% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 25.4 MB, less than 49.40% of Python3 online submissions for Daily Temperatures.
# It took 28 minutes to solve

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)        # [0, 0, 0, 0, 0, 0, 0, 0]

        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                day = stack.pop()
                answer[day] = (idx - day)

            stack.append(idx)

        return answer


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
