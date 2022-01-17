# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 322_coin_change
@time: 2021/12/5 1:51 上午
@desc: 
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        状态方程
        :param coins:
        :param amount:
        :return:
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    s = Solution()
    print(s.coinChange(coins, amount))
