# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2596_check_knight_tour.py
@time: 2023-09-13 11:54:45 
"""
from typing import List
from collections import defaultdict


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False

        count = defaultdict(tuple)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                count[grid[i][j]] = (i, j)
        pre_i, pre_j = 0, 0
        for i in range(1, m * n):
            cur_i, cur_j = count[i]
            if (abs(cur_i - pre_i) == 1 and abs(cur_j - pre_j) == 2) or (
                    abs(cur_i - pre_i) == 2 and abs(cur_j - pre_j) == 1):
                pre_i, pre_j = cur_i, cur_j
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    grid = [[8, 3, 6],
            [5, 0, 1],
            [2, 7, 4]]
    print(s.checkValidGrid(grid))
