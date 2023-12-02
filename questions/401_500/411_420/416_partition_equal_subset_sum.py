# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 416_partition_equal_subset_sum.py
@time: 2023-11-09 01:10:08 
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        target = nums_sum // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] + dp[t - num]
                print(dp)
        return dp[target] > 0


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        pass


if __name__ == '__main__':
    s = Solution2()
    nums = [1, 5, 11, 5]
    print(s.canPartition(nums))