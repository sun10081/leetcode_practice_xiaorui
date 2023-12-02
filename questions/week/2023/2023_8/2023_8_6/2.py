# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/8/6 10:46 AM
@desc:
"""
from typing import List
from itertools import accumulate


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        pre_sum = list(accumulate(nums, initial=0))
        left, right = 0, n - 1
        while left < right:
            if nums[left] > nums[right]:
                right -= 1
            else:
                pre_sum = [0] + list(map(lambda x: x - nums[left], pre_sum[1:]))
                left += 1
            if right - left == 1:
                if pre_sum[right + 1] >= m:
                    return True
                else:
                    return False
            if pre_sum[right + 1] < m:
                return False
        return True

    def canSplitArray1(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n in (1, 2):
            return True
        for i in range(n - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 3, 2, 3]
    m = 6
    print(s.canSplitArray1(nums, m))
