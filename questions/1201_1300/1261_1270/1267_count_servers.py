# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1267_count_servers.py
@time: 2023-08-24 01:50:16 
"""
from typing import List
from collections import Counter


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = Counter(), Counter()
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        return ans


class Solution2:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = Counter(), Counter()
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [[1, 0], [1, 1]]
    s = Solution2()
    print(s.countServers(grid))
