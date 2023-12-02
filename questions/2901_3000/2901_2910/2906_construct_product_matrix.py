# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2906_construct_product_matrix.py
@time: 2023-10-18 02:26:05 
"""
from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suf
                suf = grid[i][j] * suf % mod

        pre = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = p[i][j] * pre % mod
                pre = pre * grid[i][j] % mod
        return p


            
