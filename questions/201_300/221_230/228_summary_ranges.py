# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 228_summary_ranges.py
@time: 2023-08-26 23:49:01 
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            start = i
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            s = str(nums[start])
            if start < i:
                s += "->" + str(nums[i])
            ans.append(s)
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [0, 2, 3, 4, 6, 7, 9]
    print(s.summaryRanges(nums))
