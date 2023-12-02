# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1475_final_prices.py
@time: 2022-09-01 12:35:10 
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        for i in range(n):
            j = i + 1
            while j <= n - 1 and prices[j] > prices[i]:
                j += 1
            ans[i] = prices[i] if j > n - 1 else prices[i] - prices[j]
        return ans


if __name__ == '__main__':
    prices = [10,1,1,6]
    s = Solution()
    print(s.finalPrices(prices))
