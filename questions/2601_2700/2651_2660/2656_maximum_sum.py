# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2656_maximum_sum.py
@time: 2023-11-15 00:54:22 
"""
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = max(nums)
        return ans * k + k * (k - 1) // 2


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    k = 3
    s = Solution()
    print(s.maximizeSum(nums, k))