# coding=utf-8

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]- prices[i] - fee)
        :param prices:
        :return:
        """
        l = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0] - fee

        for i in range(l):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)

        return dp_i_0


if __name__ == '__main__':
    prices = [1,3,7,5,10,3]
    fee = 3
    s = Solution()
    print(s.maxProfit(prices, fee))

