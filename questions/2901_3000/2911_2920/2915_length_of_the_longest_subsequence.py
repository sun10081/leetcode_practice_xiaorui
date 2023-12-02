# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2915_length_of_the_longest_subsequence.py
@time: 2023-11-09 01:21:46 
"""
from math import inf
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [0] + [-inf] * target
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = max(dp[t], dp[t - num] + 1)
                print(dp)
        return dp[target] if dp[target] > 0 else -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 5, 4, 5]
    target = 3
    print(s.lengthOfLongestSubsequence(nums, target))