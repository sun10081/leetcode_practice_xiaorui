# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/11/5 10:24 AM
@desc:
"""
from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        one_max = 0
        ans = -1
        n = len(grid)
        for i in range(n):
            one_count = 0
            for g in grid[i]:
                if g == 1:
                    one_count += 1
            if one_count > one_max:
                one_max = one_count
                ans = i
        return ans