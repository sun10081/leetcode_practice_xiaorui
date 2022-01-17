# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 807_skyline
@time: 2021/12/13 10:34 上午
@desc: 
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0] * n
        col_max = [0] * n
        for i in range(n):
            for j in range(n):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        ans = 0

        for i in range(n):
            for j in range(n):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
        return ans

    def maxIncreaseKeepingSkyline2(self, grid: List[List[int]]) -> int:
        row_max = list(map(max, grid))
        col_max = list(map(max, zip(*grid)))
        return sum(min(row_max[i], col_max[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))

    def maxIncreaseKeepingSkyline3(self, grid: List[List[int]]) -> int:
        row_max = list(map(max, grid))
        col_max = list(map(max, zip(*grid)))
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
        return ans


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    s = Solution()
    print(s.maxIncreaseKeepingSkyline2(grid))
