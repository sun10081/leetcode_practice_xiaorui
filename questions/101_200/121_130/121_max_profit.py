# coding=utf-8

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in (0, 1):
            return 0
        start, end = 1, len(prices) - 1
        profit = prices[end] - prices[0]

        while (end - start) > 1:
            if prices[start] >= prices[end]:
                start += 1
            elif prices[start] < prices[end]:
                end -= 1
            profit = max(profit, (prices[end] - prices[start]))

        return max(0, profit)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0] * 2 for _ in range(l)]
        dp[-1][0] = 0
        dp[-1][1] = -prices[0]
        for i in range(0, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return dp[l - 1][0]


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], - prices[i])
        :param prices:
        :return:
        """
        l = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(0, l):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0


class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], -prices[i])
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
                dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        l = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(l):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, -prices[i])
        return dp0



if __name__ == '__main__':
    c = Solution3()
    a = [7, 1, 5, 3, 6, 4]
    # print(a[-1])
    print(c.maxProfit(a))
