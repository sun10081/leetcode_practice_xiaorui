# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2824_count_pairs.py
@time: 2023-08-21 21:52:23 
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1
        return ans

    def countPairs2(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            while l < r and nums[l] + nums[r] >= target:
                r -= 1
            ans += r - l
            l += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 1, 2, 3, 1]
    target = 2
    print(s.countPairs2(nums, target))
