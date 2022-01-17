# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 695_max_area_of_Island
@time: 2021/12/20 12:45 上午
@desc: 
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                grid[x][y] = 0
                res = 1
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    res += dfs(nx, ny)
                return res
            else:
                return 0

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = dfs(i, j)
                    ans = max(area, ans)
        return ans


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < m and 0 <= y < n and grid[x][y] and not visited[x][y]):
                return 0

            visited[x][y] = True
            cnt = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                cnt += dfs(nx, ny)
            return cnt

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    area = dfs(i, j)
                    ans = max(ans, area)
        return ans


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    s = Solution2()
    print(s.maxAreaOfIsland(grid))



