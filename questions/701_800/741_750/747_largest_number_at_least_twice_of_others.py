# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 747_largest_number_at_least_twice_of_others.py
@time: 2022-01-13 00:11:38 
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        first, second = nums[0], -1
        index = 0
        for i in range(1, n):
            if nums[i] > first:
                first, second = nums[i], first
                index = i
            elif nums[i] > second:
                if nums[i] >= 51:
                    return -1
                second = nums[i]
        return index if nums[index] >= 2 * second else -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    print(s.dominantIndex(nums))
