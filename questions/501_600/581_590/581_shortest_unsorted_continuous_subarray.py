# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 581_shortest_unsorted_continuous_subarray.py
@time: 2023-10-27 21:44:22 
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        l_same, r_same = 0, 0
        while l < n - 1:
            if nums[l] > nums[l + 1]:
                break
            if nums[l] == nums[l + 1]:
                l_same += 1
            l += 1
        if l == n - 1:
            return 0
        while r > 0:
            if nums[r] < nums[r - 1]:
                break
            if nums[r] == nums[r - 1]:
                r_same += 1
            r -= 1
        if r == 0:
            return 0
        return r + r_same - l - l_same + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        r, r_max = -1, - 10 ** 5 - 1
        for i in range(n):
            if nums[i] < r_max:
                r = i
            else:
                r_max = nums[i]
        l, l_min = -1, 10 ** 5 + 1
        for i in range(n - 1, -1, -1):
            if nums[i] > l_min:
                l = i
            else:
                l_min = nums[i]
        return 0 if r == -1 else r - l + 1


if __name__ == '__main__':
    s = Solution2()
    nums = [1, 2, 2, 2, 3, 2, 2, 2]
    print(s.findUnsortedSubarray(nums))
