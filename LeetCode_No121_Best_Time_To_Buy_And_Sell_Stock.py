import sys


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0

        answer = 0
        max_p = 0
        min_p = 10001                                   # 조건에서 price[i] <= 10^4 라고 했기 때문

        for p in prices:                                # brute force로 풀면 O(n^2)
            if p >= min_p:                               # O(n)으로 풀 수 있다
                max_p = max(max_p, p)
            else:
                answer = max(answer, max_p - min_p)
                min_p = p
                max_p = p

        return max(answer, max_p - min_p)


# 책에서 푼 내용
    def maxProfit2(self, prices) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)

        return profit

a = Solution()
print(a.maxProfit([3,2,6,5,0,3]))
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1]))