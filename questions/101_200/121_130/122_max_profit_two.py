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


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices))
