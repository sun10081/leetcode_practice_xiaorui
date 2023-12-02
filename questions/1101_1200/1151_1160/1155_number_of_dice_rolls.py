# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1155_number_of_dice_rolls.py
@time: 2023-10-26 10:05:28 
"""
from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        f = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for x in range(1, k + 1):
                    if x <= j:
                        f[i][j] = (f[i][j] + f[i - 1][j - x]) % mod
        return f[n][target]