# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2023_10_20
@time: 2023/10/20 4:25 PM
@desc:
"""
from typing import List
from collections import defaultdict


class Solution:

    def two_sum(self, nums: List, target: int) -> List:
        count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if target - nums[i] in count:
                return [i, count[target - nums[i]]]
            count[nums[i]] = i
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5]
    print(s.two_sum(nums, 7))
