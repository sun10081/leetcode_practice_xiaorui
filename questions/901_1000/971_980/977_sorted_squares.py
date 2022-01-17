# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 977_sorted_squares
@time: 2021/12/15 12:44 上午
@desc: 
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        pos = n - 1
        ans = [0] * n
        while left <= right:
            if nums[left] * nums[left] <= nums[right] * nums[right]:
                ans[pos] = nums[right] * nums[right]
                right -= 1
            else:
                ans[pos] = nums[left] * nums[left]
                left += 1
            pos -= 1
        return ans


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        pos = n - 1
        ans = [0] * n
        while left <= right:
            if nums[left] * nums[left] <= nums[right] * nums[right]:
                ans[pos] = nums[right] * nums[right]
                right -= 1
            else:
                ans[pos] = nums[left] * nums[left]
                left += 1
            pos -= 1
        return ans


class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        pos = n - 1
        ans = [0] * n
        while left <= right:
            if nums[left] * nums[left] <= nums[right] * nums[right]:
                ans[pos] = nums[right] * nums[right]
                right -= 1
            else:
                ans[pos] = nums[left] * nums[left]
                left += 1
            pos -= 1
        return ans


if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
    s = Solution3()
    print(s.sortedSquares(nums))
