# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 153_find_minimum.py
@time: 2023-10-31 17:04:47 
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[-1]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(s.findMin(nums))