# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 72_edit_distance.py
@time: 2023-11-11 15:07:01 
"""
from functools import lru_cache, cache
from questions.public.time_decorator import timer_decorator


class Solution:
    def minDistance1(self, word1: str, word2: str) -> int:
        @lru_cache
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1))

        return dfs(len(word1) - 1, len(word2) - 1) + 1

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(word1):
            dp[i + 1][0] = i + 1
            for j, y in enumerate(word2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[m][n]


class Solution2:
    @timer_decorator
    def minDistance1(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

        m, n = len(word1), len(word2)
        return dfs(m - 1, n - 1)

    @timer_decorator
    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = list(range(n + 1))
        for i, x in enumerate(word1):
            dp[i + 1][0] = i + 1
            for j, y in enumerate(word2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[m][n]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    s = Solution2()
    print(s.minDistance2(word1, word2))

