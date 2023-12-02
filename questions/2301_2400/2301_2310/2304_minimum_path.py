# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2304_minimum_path.py
@time: 2023-11-22 10:59:05 
"""
from typing import List
from math import inf


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]
        dp[0] = grid[0]

        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + grid[i][j] + moveCost[grid[i - 1][k]][j])
        return min(dp[m - 1])


if __name__ == '__main__':
    grid = [[5, 3], [4, 0], [2, 1]]
    moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    s = Solution()
    print(s.minPathCost(grid, moveCost))
