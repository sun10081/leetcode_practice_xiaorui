# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/10/15 10:29 AM
@desc:
"""
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)

        for i in range(0, n):
            for j in range(i, n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    indexDifference = 2
    valueDifference = 4
    print(s.findIndices(nums, indexDifference, valueDifference))
