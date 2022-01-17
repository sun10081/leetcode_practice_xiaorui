# coding=utf-8


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 在原数组上直接修改
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 1-->2
        for i in range(m):
            for j in range(n):
                obstacleGrid[i][j] = obstacleGrid[i][j] - 1

        # 2-->3
        ver_first_stone, hon_first_stone = 101, 101
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if obstacleGrid[i][j] != 0:
                        obstacleGrid[i][j] = 1
                    if obstacleGrid[i][j] == 0:
                        if i == 0:
                            hon_first_stone = min(hon_first_stone, j)
                        if j == 0:
                            ver_first_stone = min(ver_first_stone, i)

        # 3-->4
        for i in range(m):
            if i > ver_first_stone:
                obstacleGrid[i][0] = 0
        for j in range(n):
            if j > hon_first_stone:
                obstacleGrid[0][j] = 0

        # 4-->5
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == -1:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[m - 1][n - 1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp二维数组

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # 初始化第一行、第一列
        for i in range(m):
            if obstacleGrid[i][0] != 0:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] != 0:
                break
            dp[0][j] = 1

        # 根据状态转移方程 dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 进行递推
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp一维数组

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n

        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if j >= 1 and obstacleGrid[i][j - 1] == 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution3()
    obstacleGrid = [[0, 0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))
