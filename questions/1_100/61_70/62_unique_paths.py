# coding=utf-8
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1

        # dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        # f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)




if __name__ == '__main__':
    m = 3
    n = 7
    s = Solution1()
    print(s.uniquePaths2(m, n))
