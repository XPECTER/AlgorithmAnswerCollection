from collections import defaultdict, deque
from typing import List


# Runtime: 113 ms, faster than 38.50% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 14.9 MB, less than 52.70% of Python3 online submissions for Reconstruct Itinerary.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        dic = defaultdict(list)

        for ticket in sorted(tickets, reverse=True):
            dic[ticket[0]].append(ticket[1])    # DFS 돌리기 위한 그래프화

        print(dic)

        def dfs(airport):
            while dic[airport]:
                dfs(dic[airport].pop())
            answer.append(airport)
            return

        dfs("JFK")

        return answer[::-1]


if __name__ == "__main__":
    # print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
