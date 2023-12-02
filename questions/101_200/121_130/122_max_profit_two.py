# coding=utf-8

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]- prices[i])
        :param prices:
        :return:
        """
        l = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(l):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]- prices[i])
        :param prices:
        :return:
        """
        l = len(prices)
        dp = [[0] * 2 for _ in range(l)]
        for i in range(l):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        l = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(l):
            temp = dp0
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, temp - prices[i])
        return dp0


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices))
