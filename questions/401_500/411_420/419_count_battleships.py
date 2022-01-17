# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 419_count_battleships
@time: 2021/12/18 8:59 上午
@desc: 
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if i > 0 and board[i - 1][j] == 'X':
                        continue
                    if j > 0 and board[i][j - 1] == 'X':
                        continue
                    ans += 1
        return ans

    def countBattleships2(self, board: List[List[str]]) -> int:
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < m and 0 <= y < n and board[x][y] == 'X'):
                return 0
            cnt = 0
            board[x][y] = '.'
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                cnt += dfs(nx, ny)
            return cnt + 1

        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
        return ans

    def countBattleships3(self, board: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] == '.':
                return False
            board[i][j] = '.'
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(i + dx, j + dy)
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j)
        return 2


if __name__ == '__main__':
    s = Solution()
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    print(s.countBattleships3(board))
