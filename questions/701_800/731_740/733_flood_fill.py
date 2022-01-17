# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 733_flood_fill
@time: 2021/12/18 8:53 下午
@desc: 
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(x: int, y: int):
            if 0 <= x < m and 0 <= y < n and image[x][y] == original_color and not visited[x][y]:
                image[x][y] = newColor
                visited[x][y] = True
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    dfs(nx, ny)
            else:
                return

        m, n = len(image), len(image[0])
        visited = [[False] * n for _ in range(m)]
        original_color = image[sr][sc]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dfs(sr, sc)
        return image


class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(x: int, y: int) -> None:
            if 0 <= x < m and 0 <= y < n and image[x][y] == original_color and not visited[x][y]:
                visited[x][y] = True
                image[x][y] = newColor
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    dfs(nx, ny)
            else:
                return

        m, n = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        original_color = image[sr][sc]
        dfs(sr, sc)
        return image


if __name__ == '__main__':
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    solution = Solution2()
    print(solution.floodFill(image, sr, sc, newColor))
