# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 463_island_perimeter
@time: 2021/12/7 7:39 下午
@desc: 
"""
from typing import List, Tuple


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cnt = 0
                    for x, y in directions:
                        nx, ny = i + x, j + y
                        if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1):
                            cnt += 1
                    ans += cnt
        return ans

    def islandPerimeterDFS(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, grid: List[List[int]], directions: List[Tuple[int, int]]) -> int:
            # 因为更改了值为2，所以不好用这个判断 not (0 <= x < m and 0 <= y < n and grid[x][y] == 1):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0
            # 遍历过的格子赋值 避免重复遍历
            grid[x][y] = 2
            res = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                res += dfs(nx, ny, grid, directions)
            return res

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += dfs(i, j, grid, directions)
                    # 找到一个网格即可搜索完全部岛屿 不需要继续遍历了
                    break
        return ans

    def islandPerimeterBfs(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop()
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                            ans += 1
                            continue
                        if grid[x][y] == 2:
                            continue
                        grid[x][y] = 2
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            queue.append((nx, ny))
                    # 找到一个网格即可搜索完全部岛屿 不需要继续遍历了
                    if ans:
                        return ans
        return ans


class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        朴素写法
        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for x, y in directions:
                        nx, ny = x + i, y + j
                        if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny]):
                            ans += 1
        return ans

    def islandPerimeterDFS1(self, grid: List[List[int]]) -> int:
        """
        第一种dfs 不允许修改原数组
        :param grid:
        :return:
        """

        def dfs(x: int, y: int) -> int:
            if not (0 <= x < m and 0 <= y < n and grid[x][y]):
                return 1
            if visited[x][y]:
                return 0
            visited[x][y] = True
            cnt = 0
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                cnt += dfs(nx, ny)
            return cnt

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += dfs(i, j)
        return ans

    def islandPerimeterDFS2(self, grid: List[List[int]]) -> int:
        """
        第二种dfs 修改原数组，不需要visited数组 体会区别
        :param grid:
        :return:
        """

        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0
            grid[x][y] = 2
            cnt = 0
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                cnt += dfs(nx, ny)
            return cnt

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += dfs(i, j)
        return ans


class Solution3:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            # if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
            #     return 0
            cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1):
                    cnt += 1
            return cnt

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
        return ans

    def islandPerimeterDFS(self, grid: List[List[int]]) -> int:
        """
        不修改数组
        :param grid:
        :return:
        """

        def dfs(x: int, y: int) -> int:
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == 1):
                return 1
            if visited[x][y]:
                return 0

            visited[x][y] = True
            cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                cnt += dfs(nx, ny)
            return cnt

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
        return ans


class Solution4:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < m and 0 <= y < n and grid[x][y]):
                return 1
            if visited[x][y]:
                return 0
            visited[x][y] = True

            cnt = 0
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
                    ans += dfs(i, j)
                    return ans
        return -1


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

    s = Solution4()
    print(s.islandPerimeter(grid))
