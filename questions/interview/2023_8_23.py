# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2023_8_23
@time: 2023/8/23 3:45 PM
@desc:
"""
from typing import List
from collections import defaultdict


class Solution:

    def two_sum(self, nums: List, target: int) -> List:
        ans = []
        if not nums:
            return ans
        count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if target - nums[i] in count:
                ans.append([i, count[target - nums[i]]])
            else:
                count[nums[i]] = i
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    target = 5
    print(s.two_sum(nums, target))