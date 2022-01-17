# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 542_update_matrix
@time: 2021/12/22 9:26 下午
@desc: 
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def dfs(x: int, y: int, path: int):
            if mat[x][y] == 0:
                return path

            tmp_path = float("inf")
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if mat[nx][ny] == 0:
                        return path + 1
                    else:
                        visited[nx][ny] = True
                        tmp_path = min(tmp_path, dfs(nx, ny, path + 1))
                        visited[nx][ny] = False
            return tmp_path

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                mat[i][j] = dfs(i, j, 0)
        return mat


if __name__ == '__main__':
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    s = Solution()
    print(s.updateMatrix(mat))
