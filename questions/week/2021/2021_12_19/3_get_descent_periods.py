# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3_get_descent_periods
@time: 2021/12/19 11:12 上午
@desc: 
"""
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        con = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                con += 1
            else:
                con = 1
            if con == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + con
        return dp[-1]

    def getDescentPeriods2(self, prices: List[int]) -> int:
        """
        dp 滚动数组
        :param prices:
        :return:
        """
        n = len(prices)
        if n == 1:
            return 1
        dp1 = 1
        dp2 = 1
        con = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                con += 1
            else:
                con = 1
            if con == 1:
                dp2 = dp1 + 1
            else:
                dp2 = dp1 + con
            dp1 = dp2
        return dp2


if __name__ == '__main__':
    prices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 3, 10, 9, 8, 7]
    # prices = [5, 4, 3, 2, 1]
    s = Solution()
    print(s.getDescentPeriods2(prices))
