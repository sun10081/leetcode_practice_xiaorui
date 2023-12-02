# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1658_minimum_operations.py
@time: 2023-01-07 09:26:28 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)

        if total < x:
            return -1

        r = 0
        l_sum, r_sum = 0, total
        ans = n + 1
        for l in range(-1, n - 1):
            if l != -1:
                l_sum += nums[l]
            while r < n and l_sum + r_sum > x:
                r_sum -= nums[r]
                r += 1
            if l_sum + r_sum == x:
                ans = min(ans, l + 1 + n - r)

        return -1 if ans > n else ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 4, 2, 3]
    x = 5
    print(s.minOperations(nums, x))
