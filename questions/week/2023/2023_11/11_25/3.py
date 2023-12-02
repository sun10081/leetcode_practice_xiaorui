# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 3
@time: 2023/11/25 10:27 PM
@desc:
"""
from typing import List
from math import inf
from functools import cache


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] + [inf] * n
        for i in range(n):
            for j in range(i + 1, min(n, 2 * (i + 1)) + 1):
                dp[j] = min(dp[j], dp[i] + prices[i])
        return dp[n]

    def minimumCoins2(self, prices: List[int]) -> int:
        @cache
        def dfs(i):
            if i * 2 >= n:
                return prices[i - 1]
            ans = inf
            for j in range(i + 1, 2 * i + 2):
                ans = min(ans, dfs(j))
            return ans + prices[i - 1]
        n = len(prices)
        return dfs(1)

    def minimumCoins3(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        for i in range(n, 0, -1):
            if i * 2 >= n:
                dp[i] = prices[i - 1]
            else:
                dp[i] = min(dp[i + 1: i * 2 + 2]) + prices[i - 1]
        return dp[1]


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = Solution()
    print(s.minimumCoins(prices))
