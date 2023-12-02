# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 494_target_sum.py
@time: 2023-11-08 22:03:00 
"""
from typing import List
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache
        def dfs(i, t):
            if i < 0:
                return 1 if t == 0 else 0
            if t < nums[i]:
                return dfs(i - 1, t)
            return dfs(i - 1, t) + dfs(i - 1, t - nums[i])

        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)
        return dfs(n - 1, target)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for t in range(target + 1):
                if t < x:
                    f[i + 1][t] = f[i][t]
                else:
                    f[i + 1][t] = f[i][t] + f[i][t - x]
        return f[n][target]

    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for x in nums:
            for t in range(target, x - 1, -1):
                if t >= x:
                    f[t] = f[t] + f[t - x]
        return f[target]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(s.findTargetSumWays3(nums, target))
