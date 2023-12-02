# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 931_minimum_falling_path_sum.py
@time: 2023-07-13 23:56:59 
"""
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [matrix[0]]
        n = len(matrix)

        for i in range(1, n):
            cur = [0] * n
            for j in range(n):
                mn = dp[i - 1][j]
                if j > 0:
                    mn = min(mn, dp[i - 1][j - 1])
                if j < n - 1:
                    mn = min(mn, dp[i - 1][j + 1])
                cur[j] = mn + matrix[i][j]
            dp.append(cur)
        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    matrix = [[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]
    print(s.minFallingPathSum(matrix))
