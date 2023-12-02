# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 75_sort_colors.py
@time: 2023-08-10 02:57:14 
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return

        i = 0
        p0, p2 = 0, n - 1
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1:
            return

        i = 0
        p0, p2 = 0, n - 1
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1


if __name__ == '__main__':
    nums = [2, 0, 1]
    s = Solution()
    s.sortColors(nums)
    print(nums)