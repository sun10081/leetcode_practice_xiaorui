# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 279_perfect_squares.py
@time: 2023-11-09 00:31:05 
"""
from math import inf
from typing import List


class Solution:
    nums = [i * i for i in range(1, 101)]

    def numSquares(self, n: int) -> int:
        dp = [inf] * (n + 1)
        dp[0] = 0
        for num in self.nums:
            for t in range(num, n + 1):
                dp[t] = min(dp[t], dp[t - num] + 1)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    n = 12
    print(s.numSquares(n))

