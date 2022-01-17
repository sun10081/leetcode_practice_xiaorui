# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 130_surrounded_regions
@time: 2021/12/18 9:18 下午
@desc: 
"""
from typing import List


class Solution:
    def surrounded_regions(self, board: List[List[str]]) -> None:
        def dfs(x: int, y: int):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != "O":
                return
            board[x][y] = "A"
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                dfs(nx, ny)

        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s = Solution()
    s.surrounded_regions(board)
    print(board)
