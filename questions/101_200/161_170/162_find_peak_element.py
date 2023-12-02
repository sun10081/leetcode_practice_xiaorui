# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 162_find_peak_element.py
@time: 2023-10-31 16:54:43 
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l