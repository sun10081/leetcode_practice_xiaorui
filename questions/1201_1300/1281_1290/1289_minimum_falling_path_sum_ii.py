# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1289_minimum_falling_path_sum_ii.py
@time: 2023-08-10 15:41:12 
"""
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[10**9 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, n):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + grid[i][j])
        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.minFallingPathSum(grid))
                    
        