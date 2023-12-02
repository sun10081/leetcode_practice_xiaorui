# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1464_maximum_product_of_two_elements_in_an_array.py
@time: 2022-08-26 12:44:45 
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = nums[0], nums[1]
        if first < second:
            first, second = second, first
        for i in range(2, len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return (first - 1) * (second - 1)


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    s = Solution()
    print(s.maxProduct(nums))
