# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 209_minimum_size_subarray_sum.py
@time: 2023-10-30 23:11:31 
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = 10 ** 5 + 1
        l = 0
        cur_sum = 0
        for r in range(n):
            cur_sum += nums[r]
            while cur_sum - nums[l] >= target:
                cur_sum -= nums[l]
                l += 1
            if cur_sum >= target:
                ans = min(ans, r - l + 1)
        return ans if ans < 10 ** 5 + 1 else 0


if __name__ == '__main__':
    s = Solution()
    target = 15
    nums = [1, 2, 3, 4, 5]
    print(s.minSubArrayLen(target, nums))
