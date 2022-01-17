# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 994_rotting_oranges
@time: 2021/12/22 4:51 下午
@desc: 
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not any([any(array) for array in grid]):
            return 0
        queue = []
        ans = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        while queue:
            tmp_queue = queue[:]
            queue = []
            while tmp_queue:
                x, y = tmp_queue.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
            ans += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans - 1


if __name__ == '__main__':
    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # s = Solution()
    # print(s.orangesRotting(grid))

    grid = [[0]]
    print(any([any(array) for array in grid]))
