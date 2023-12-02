
# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/9/10 10:29 AM
@desc:
"""
from typing import List
from collections import defaultdict


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        count = defaultdict(int)
        for start, end in nums:
            for i in range(start, end + 1):
                count[i] += 1
        return len(count)


if __name__ == '__main__':
    s = Solution()
    nums = [[3,6],[1,5],[4,7]]
    print(s.numberOfPoints(nums))
