# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 137_single_number_ii.py
@time: 2023-10-15 15:30:19 
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31):
            total = sum(num >> i & 1 for num in nums)
            ans |= total % 3 << i
        total = sum(num >> 31 & 1 for num in nums)
        return ans - (total % 3 << 31)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
    a = -4 >> 10
    print(a)
    # print(s.singleNumber(nums))
