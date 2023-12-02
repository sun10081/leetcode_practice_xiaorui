# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2948_make_smallest_array_by_swapping.py
@time: 2023-11-29 18:59:11 
"""
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted(zip(nums, range(n)))
        ans = [-1] * n
        i = 0
        while i < n:
            st = i
            i += 1
            while i < n and arr[i][0] - arr[i - 1][0] <= limit:
                i += 1
            idx = sorted(j for _, j in arr[st:i])
            for j, (x, _) in zip(idx, arr[st:i]):
                ans[j] = x
        return ans

