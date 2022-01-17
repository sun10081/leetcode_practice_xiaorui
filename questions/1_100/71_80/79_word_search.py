# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 79_word_search
@time: 2021/12/18 10:47 下午
@desc: 
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, index: int):
            # print(word[0:index+1])
            if board[x][y] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            visited[x][y] = True
            flag = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if dfs(nx, ny, index + 1):
                        flag = True
                        break
            visited[x][y] = False
            return flag

        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, begin_index: int) -> bool:
            if board[x][y] != word[begin_index]:
                return False
            if begin_index == len(word) - 1:
                return True

            flag = False
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if dfs(nx, ny, begin_index + 1):
                        flag = True
                        break
            visited[x][y] = False
            return flag

        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


class Solution3:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, begin_index: int) -> bool:
            if word[begin_index] != board[x][y]:
                return False
            if begin_index == len(word) - 1:
                return True

            visited[x][y] = True
            flag = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny <n and not visited[nx][ny]:
                    if dfs(nx, ny, begin_index + 1):
                        flag = True
                        break
            visited[x][y] = False
            return flag

        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    s = Solution3()
    print(s.exist(board, word))

