# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2918_minimum_equal_sum.py
@time: 2023-11-03 01:31:39 
"""
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zero1 = sum(nums1), nums1.count(0)
        sum2, zero2 = sum(nums2), nums2.count(0)

        if zero1 == 0 and zero2 == 0:
            return -1 if sum1 != sum2 else sum1

        sum1 += zero1
        sum2 += zero2
        if sum1 == sum2:
            return sum1
        elif sum1 > sum2 and zero2 != 0:
            return sum1
        elif sum2 > sum1 and zero1 != 0:
            return sum2
        return -1


if __name__ == '__main__':
    s = Solution()
    nums1 = [3, 2, 0, 1, 0]
    nums2 = [6, 5, 0]
    print(s.minSum(nums1, nums2))