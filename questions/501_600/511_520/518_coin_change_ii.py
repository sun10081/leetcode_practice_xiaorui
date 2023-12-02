# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 518_coin_change_ii.py
@time: 2023-11-09 00:47:20 
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for t in range(coin, amount + 1):
                dp[t] = dp[t] + dp[t - coin]
                print(dp)
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(s.change(amount, coins))
