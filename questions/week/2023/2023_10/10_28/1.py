# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/10/28 10:27 PM
@desc:
"""
from typing import List
from collections import Counter, defaultdict


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        window = 2
        count = defaultdict()
        l, r = 0, 0
        ans = n
        while window < n:
            while r < n:
                while r - l + 1 < window:
                    r += 1
                    count[nums[r]] += 1



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,1]
    print(s.sumCounts(nums))