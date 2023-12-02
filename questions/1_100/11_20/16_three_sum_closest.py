# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 16_three_sum_closest.py
@time: 2023-07-10 16:48:01 
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = []
        n = len(nums)
