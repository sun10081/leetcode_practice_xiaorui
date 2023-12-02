# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2760_longest_even_odd_subarray.py
@time: 2023-11-16 00:11:25
"""
from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l = 0
        arr = []
        while l < n:
            if not nums[l] % 2 and nums[l] <= threshold:
                arr.append(l)
            l += 1
        ans = 0
        for j in arr:
            ans = max(ans, self.get_sub_array_len(nums, j, threshold))
        return ans

    def get_sub_array_len(self, nums: List[int], l: int,threshold: int) -> int:
        ans = 1
        r = l
        even = False
        while r < len(nums) - 1:
            r += 1
            if nums[r] <= threshold and (even and not nums[r] % 2 or not even and nums[r] % 2):
                ans = max(ans, r - l + 1)
            else:
                return ans
            even = not even
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [4, 10, 3]
    threshold = 10
    print(s.longestAlternatingSubarray(nums, threshold))