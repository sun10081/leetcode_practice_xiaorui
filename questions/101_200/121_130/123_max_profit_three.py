# coding=utf-8

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][1][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        dp[i][1][1] = max(dp[i - 1][k][1], dp[i - 1][k-1][0] - prices[i])
        :param prices:
        :return:
        """
        max_k = 2
        l = len(prices)
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
    k = 2
    prices = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.maxProfit(prices))
