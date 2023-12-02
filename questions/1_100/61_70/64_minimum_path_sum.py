# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 64_minimum_path_sum.py
@time: 2023-07-28 02:37:25 
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i] = grid[0][0]
                elif i == 0:
                    dp[j] += grid[0][j - 1]
                elif j == 0:
                    dp[0] += grid[i][0]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(s.minPathSum(grid))


