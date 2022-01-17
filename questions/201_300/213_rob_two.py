# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 213_rob_two
@time: 2021/12/4 1:30 上午
@desc: 
"""
from typing import List


class Solution:
    def rob_two(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[0]
        second = max(first, nums[1])
        for i in range(2, n):
            first, second = second, max(second, first + nums[i])
        return second


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums: List[int]) -> int:
        first, second = 0, nums[0]
        for i in range(1, len(nums)):
            first, second = second, max(second, first + nums[i])
        return second


if __name__ == '__main__':
    nums = [2, 3, 2]
    s = Solution2()
    print(s.rob(nums))
