# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2216_minimum_deletions.py
@time: 2023-11-21 01:37:02 
"""
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        cur, ans = 0, 0
        n = len(nums)
        while cur < n:
            stack.append(nums[cur])
            cur += 1
            while cur < n and stack[-1] == nums[cur]:
                cur += 1
                ans += 1
            if cur < n:
                stack.append(nums[cur])
            else:
                stack.pop()
                ans += 1
            cur += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 2, 3, 3]
    print(s.minDeletion(nums))
