# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 334_increasing_triplet_subsequence.py
@time: 2022-01-12 10:17:24 
"""
import bisect
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for i in range(len(nums)):
            if not lis or nums[i] > lis[-1]:
                lis.append(nums[i])
                if len(lis) == 3:
                    return True
            else:
                loc = bisect.bisect_left(lis, nums[i])
                lis[loc] = nums[i]
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float('inf')
        for i in range(1, n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False


class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float("inf")
        for i in range(1, n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False


if __name__ == '__main__':
    nums = [2, 4, -2, -3]
    s = Solution2()
    print(s.increasingTriplet(nums))
