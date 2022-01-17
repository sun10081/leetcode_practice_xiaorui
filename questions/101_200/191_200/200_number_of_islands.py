# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 200_number_of_islands
@time: 2021/12/7 8:21 下午
@desc: 
"""
from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int, grid: List[List[str]], directions: List[Tuple[int, int]]):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                grid[x][y] = "0"
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    dfs(nx, ny, grid, directions)
            else:
                return

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j, grid, directions)
                    ans += 1
        return ans

    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    queue = [(i, j)]
                    ans += 1
                    while queue:
                        x, y = queue.pop(0)
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            grid[x][y] = "0"
                            for dx, dy in directions:
                                nx, ny = x + dx, y + dy
                                queue.append((nx, ny))
                    # queue.clear()
        return ans


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        修改原数组
        :param grid:
        :return:
        """

        def dfs(x: int, y: int):
            # 寻找相邻为'1'的网格
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                grid[x][y] = '0'
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    dfs(nx, ny)
            else:
                return

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans

    def numIslands2(self, grid: List[List[str]]) -> int:
        """
        不修改原数组
        :param grid:
        :return:
        """

        def dfs(x: int, y: int):
            # 寻找相邻为'1'的网格
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not visited[x][y]:
                visited[x][y] = True
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    dfs(nx, ny)
            else:
                return

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans


class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == "1" and not visited[x][y]):
                return

            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans


class Solution4:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == "1" and not visited[x][y]):
                return

            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]

    ]
    s = Solution4()
    print(s.numIslands(grid))
