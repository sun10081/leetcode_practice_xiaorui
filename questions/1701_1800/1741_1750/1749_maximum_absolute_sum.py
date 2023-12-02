# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1749_maximum_absolute_sum.py
@time: 2023-08-08 00:47:27 
"""
from typing import List
from itertools import accumulate


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pre_sum = list(accumulate(nums, initial=0))
        return max(pre_sum) - min(pre_sum)

    def maxAbsoluteSum2(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        max_pre_sum = 0
        min_sum = float('inf')
        min_pre_sum = 0

        for num in nums:
            max_pre_sum = max(max_pre_sum + num, num)
            max_sum = max(max_sum, max_pre_sum)

            min_pre_sum = min(min_pre_sum + num, num)
            min_sum = min(min_sum, min_pre_sum)
        return max(max_sum, -min_sum)


if __name__ == '__main__':
    nums = [1, -3, 2, 3, -4]
    s = Solution()
    print(s.maxAbsoluteSum2(nums))