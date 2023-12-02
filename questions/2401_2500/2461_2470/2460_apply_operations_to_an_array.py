# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2460_apply_operations_to_an_array.py
@time: 2023-06-05 23:52:35 
"""
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        for i in range(n):
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


if __name__ == '__main__':
    nums = [1, 2, 2, 1, 1, 0]
    s = Solution()
    print(s.applyOperations(nums))
