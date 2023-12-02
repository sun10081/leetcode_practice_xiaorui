# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 915_partition_array.py
@time: 2023-11-10 00:08:57 
"""
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        l_max = [nums[0]]
        for i in range(1, n):
            l_max.append(max(nums[i], l_max[-1]))
        r_min = [nums[n - 1]]
        for i in range(n - 2, -1, -1):
            r_min.insert(0, min(r_min[0], nums[i]))
        for i in range(n - 1):
            if l_max[i] <= r_min[i + 1]:
                return i + 1

    def partitionDisjoint2(self, nums: List[int]) -> int:
        n = len(nums)
        lmax = nums[0]
        rmin = [0] * n
        rmin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rmin[i] = min(nums[i], rmin[i + 1])
        for i in range(1, n):
            if lmax <= rmin[i]:
                return i
            lmax = max(lmax, nums[i])

    def partitionDisjoint3(self, nums: List[int]) -> int:
        n = len(nums)
        r_min = [0] * n
        r_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            r_min[i] = min(nums[i], r_min[i + 1])
        l_max = nums[0]
        for i in range(1, n - 1):
            if l_max <= r_min[i + 1]:
                return l_max + 1
            l_max = max(l_max, nums[i])


if __name__ == '__main__':
    nums = [1, 1]
    s = Solution()
    print(s.partitionDisjoint2(nums))
