# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1034_coloring_a_border
@time: 2021/12/7 10:15 上午
@desc: 
"""
from typing import List, Tuple


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 标记网格是否被探查过
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        original_color = grid[row][col]
        # 记录连通边界
        boards = []
        self.dfs(grid, row, col, original_color, visited, boards)
        for x, y in boards:
            grid[x][y] = color
        return grid

    def dfs(self, grid: List[List[int]], x: int, y: int, original_color: int, visited: List[List[bool]],
            boards: List[Tuple]):
        is_board = False
        m, n = len(grid), len(grid[0])
        # 标记上下左右四个方向的网格
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 周围存在非连通网格 则证明此网格是连通边界
            if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == original_color):
                is_board = True
            # 周围网格是连通分量或者此网格是边界 则要判断下是否探查过，与上面的判断互斥，所以要用elif
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                self.dfs(grid, nx, ny, original_color, visited, boards)
        if is_board:
            boards.append((x, y))

    def colorBorderBfs(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 标记网格是否被探查过
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        original_color = grid[row][col]
        # 记录连通边界
        boards = []
        # 标记上下左右四个方向的网格
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 用list表示队列
        queue = [(row, col)]
        while queue:
            is_board = False
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == original_color):
                    is_board = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
            if is_board:
                boards.append((x, y))
        for x, y in boards:
            grid[x][y] = color
        return grid


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    row = 1
    col = 1
    color = 2
    s = Solution()
    print(s.colorBorderDfs(grid, row, col, color))
