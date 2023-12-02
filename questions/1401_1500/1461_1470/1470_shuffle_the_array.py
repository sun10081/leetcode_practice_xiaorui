# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1470_shuffle_the_array.py
@time: 2022-08-29 12:38:26 
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i, j = 0, n
        ans = []
        while i < n:
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        return ans

    def shuffle_1(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans

    def shuffle_2(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[1::2], nums[::2]
        return nums

