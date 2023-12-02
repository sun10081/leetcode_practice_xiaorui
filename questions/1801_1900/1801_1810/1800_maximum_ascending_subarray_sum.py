# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1800_maximum_ascending_subarray_sum.py
@time: 2022-10-07 18:58:29 
"""
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start, end = 0, 1
        cur_sum, max_sum = nums[0], nums[0]
        while end < len(nums):
            if nums[end] > nums[end - 1]:
                cur_sum += nums[end]
                max_sum = max(max_sum, cur_sum)
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[end]
            end += 1
        return max_sum


if __name__ == '__main__':
    nums = [100, 10, 1]
    s = Solution()
    print(s.maxAscendingSum(nums))
