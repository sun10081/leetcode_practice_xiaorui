# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2023_7_31
@time: 2023/7/31 4:29 PM
@desc:
"""
from typing import List


class Solution:

    def quick_sort(self, nums: List):
        self._quick_sort(nums, 0, len(nums) - 1)

    def _quick_sort(self, nums: List, l: int, r: int):
        if l >= r:
            return
        i, j = l - 1, r + 1
        x = nums[i + j >> 1]
        while i < j:
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        self._quick_sort(nums, l, j)
        self._quick_sort(nums, j + 1, r)


if __name__ == '__main__':
    nums = [50, 1, 70, 185, 60, 30, 5]
    s = Solution()
    s.quick_sort(nums)
    print(nums)