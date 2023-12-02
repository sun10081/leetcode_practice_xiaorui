# coding=utf-8

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0]- prices[i])
        :param prices:
        :return:
        """
        l = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        de_pre_0 = 0

        for i in range(l):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, de_pre_0 - prices[i])
            de_pre_0 = temp
        return dp_i_0


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0]- prices[i])
        :param prices:
        :return:
        """
        l = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        dp0_pre = 0

        for i in range(l):
            temp = dp0
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0_pre - prices[i])
            dp0_pre = temp
        return dp0


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    s = Solution()
    print(s.maxProfit(prices))
