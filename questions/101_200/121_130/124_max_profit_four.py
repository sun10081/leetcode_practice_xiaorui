# coding=utf-8

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        if l == 0:
            return 0
        max_k = min(k, l // 2)
        dp = [[[0] * 2 for _ in range(max_k + 1)] * 1 for _ in range(l)]

        for k in range(0, max_k + 1):
            dp[-1][k][0] = 0
            dp[-1][k][1] = - prices[0]

        for i in range(0, l):
            for k in range(max_k, 0, -1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[l - 1][max_k][0]


if __name__ == '__main__':
    s = Solution()
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(s.maxProfit(k, prices))
