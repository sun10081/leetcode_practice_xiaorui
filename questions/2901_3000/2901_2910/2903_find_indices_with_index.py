# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2903_find_indices_with_index.py
@time: 2023-10-17 22:45:45 
"""
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        max_num_id, min_num_id = 0, 0
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            if nums[i] > nums[max_num_id]:
                max_num_id = i
            if nums[i] < nums[min_num_id]:
                min_num_id = i
            if nums[max_num_id] - nums[j] >= valueDifference:
                return [max_num_id, j]
            if nums[j] - nums[min_num_id] >= valueDifference:
                return [min_num_id, j]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    nums = [31, 23, 36]
    indexDifference = 1
    valueDifference = 11
    print(s.findIndices(nums, indexDifference, valueDifference))
