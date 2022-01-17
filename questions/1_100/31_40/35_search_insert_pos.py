# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 35_search_insert_pos
@time: 2021/12/13 11:44 下午
@desc: 
"""
import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # [mid + 1, right]
                left = mid + 1
            else:
                # [left, mid]
                right = mid - 1
        return left

    def searchInsert2(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution3:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 6
    s = Solution3()
    print(s.searchInsert(nums, target))
