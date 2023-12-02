# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2500_delete_greatest_value.py
@time: 2023-07-27 15:40:39 
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for array in grid:
            array.sort()
        ans = 0
        for array in zip(*grid):
            ans += max(array)
        return ans


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 2, 4], [3, 3, 1]]
    print(solution.deleteGreatestValue(grid))