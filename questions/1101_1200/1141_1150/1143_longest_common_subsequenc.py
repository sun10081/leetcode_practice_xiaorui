# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1143_longest_common_subsequenc.py
@time: 2023-11-10 01:30:09 
"""
from typing import List
from questions.public.time_decorator import timer_decorator
from functools import lru_cache, cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        m, n = len(text1), len(text2)
        return dfs(m - 1, n - 1)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[m][n]


class Solution2:

    @timer_decorator
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        m, n = len(text1), len(text2)
        return dfs(m - 1, n - 1)

    @timer_decorator
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[m][n]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    s = Solution2()
    print(s.longestCommonSubsequence2(text1, text2))