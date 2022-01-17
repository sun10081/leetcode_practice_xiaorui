# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2104_sub_array_ranges
@time: 2021/12/25 10:11 下午
@desc: 
"""
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            max_value = float("-inf")
            min_value = float("inf")
            for j in range(i, n):
                max_value = max(max_value, nums[j])
                min_value = min(min_value, nums[j])
                ans += max_value - min_value
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [4, -2, -3, 4, 1]
    print(s.subArrayRanges(nums))
