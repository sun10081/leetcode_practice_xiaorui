# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 870_advantage_shuffle.py
@time: 2022-10-08 12:42:58 
"""
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        ids2 = sorted(range(n), key=lambda x: nums2[x])
        start, end = 0, n - 1
        ans = [0] * n
        for num in nums1:
            if num > nums2[ids2[start]]:
                ans[ids2[start]] = num
                start += 1
            else:
                ans[ids2[end]] = num
                end -= 1
                round
        return ans
