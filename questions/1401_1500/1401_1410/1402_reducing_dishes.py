# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1402_reducing_dishes.py
@time: 2023-10-22 22:49:12 
"""
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        前缀和
        :param satisfaction:
        :return:
        """
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        ans = 0
        n = len(satisfaction)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + satisfaction[i - 1]

        cur = 0
        for i in range(n - 1, -1, -1):
            cur += pre_sum[n] - pre_sum[i]
            if cur >= ans:
                ans = cur
            else:
                break
        return ans


class Solution2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        dp
        :param satisfaction:
        :return:
        """
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        n = len(satisfaction)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + j * satisfaction[i - 1]
                if i - 1 >= j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                ans = max(ans, dp[i][j])
        return ans

    def maxSatisfaction1(self, satisfaction: List[int]) -> int:
        """
        dp[i][j] i代表第i道菜 j代表真正选取的菜
        :param satisfaction:
        :return:
        """
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        n = len(satisfaction)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + satisfaction[i - 1] * j
                if j <= i - 1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                ans = max(ans, dp[i][j])
        return ans

    def maxSatisfaction2(self, satisfaction: List[int]) -> int:
        """
        前缀和
        :param satisfaction:
        :return:
        """
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        n = len(satisfaction)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + satisfaction[i - 1]
        cur = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            cur += pre_sum[n] - pre_sum[i]
            if cur >= ans:
                ans = cur
            else:
                break
        return ans


if __name__ == '__main__':
    s = Solution2()
    satisfaction = [-1, -8, 0, 5, -7]
    print(s.maxSatisfaction2(satisfaction))
