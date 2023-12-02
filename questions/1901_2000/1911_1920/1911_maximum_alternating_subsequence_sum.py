# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1911_maximum_alternating_subsequence_sum.py
@time: 2023-07-11 14:53:08 
"""
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        g = [0] * (n + 1)

        for i, num in enumerate(nums, start=1):
            f[i] = max(g[i - 1] - num, f[i - 1])
            g[i] = max(f[i - 1] + num, g[i - 1])

        return max(f[n], g[n])


class Solution1:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # n = len(nums)
        f, g = 0, 0

        for i, num in enumerate(nums, start=1):
            f = max(g - num, f)
            g = max(f + num, g)
        return max(f, g)
