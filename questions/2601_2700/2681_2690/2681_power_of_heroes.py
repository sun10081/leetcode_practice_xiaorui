# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2681_power_of_heroes.py
@time: 2023-08-01 22:03:15 
"""
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        dp = [0] * n
        pre_sum = [0] * (n + 1)
        mod = 10 ** 9 + 7

        for i in range(n):
            dp[i] = (nums[i] + pre_sum[i]) % mod
            pre_sum[i + 1] = (pre_sum[i] + dp[i]) % mod
            ans = (ans + nums[i] * nums[i] * dp[i]) % mod
        return ans

    def sumOfPower2(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        dp, pre_sum = 0, 0
        mod = 10 ** 9 + 7

        for i in range(n):
            dp = (nums[i] + pre_sum) % mod
            pre_sum = (pre_sum + dp) % mod
            ans = (ans + nums[i] * nums[i] * dp) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 4]
    print(s.sumOfPower(nums))
