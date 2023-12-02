# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 918_maximum_sum_circular_subarray.py
@time: 2023-07-20 10:49:38 
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        min_sum = 0
        max_pre, min_pre = 0, 0
        n = len(nums)
        for i in range(n):
            max_pre = max(nums[i], max_pre + nums[i])
            max_sum = max(max_sum, max_pre)
            min_pre = min(nums[i], min_pre + nums[i])
            min_sum = min(min_sum, min_pre)
        if min_sum == sum(nums):
            return max_sum
        return max(max_sum, sum(nums) - min_sum)


if __name__ == '__main__':
    s = Solution()
    nums = [-3, -2, -3]
    print(s.maxSubarraySumCircular(nums))
