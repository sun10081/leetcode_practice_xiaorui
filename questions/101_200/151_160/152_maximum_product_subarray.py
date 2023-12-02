# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 152_maximum_product_subarray.py
@time: 2023-11-22 20:38:19 
"""
from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_max, pre_min = 1, 1
        ans_max, ans_min = -inf, inf

        for num in nums:
            tmp = pre_max
            pre_max = max(num, pre_max * num, pre_min * num)
            pre_min = min(num, pre_min * num, tmp * num)
            ans_max = max(ans_max, pre_max)
        return ans_max


if __name__ == '__main__':
    nums = [-1, -2, -9, -6]
    s = Solution()
    print(s.maxProduct(nums))
