# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 34_search_range_in_array
@time: 2021/11/30 5:22 下午
@desc: 
"""
import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left_point(num: int) -> int:
            left, right = 0, n
            # 等号处理 [1] 1 这种bad case
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        if not nums:
            return [-1, -1]
        n = len(nums) - 1
        l = binary_search_left_point(target)
        r = binary_search_left_point(target + 1) - 1
        # 判断l范围 处理bad case nums = [2,2] target = 3
        if l == n + 1 or nums[l] != target:
            return [-1, -1]
        return [l, r]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, right]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left() -> int:
            left, right = 0, n
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        n = len(nums)
        left = binary_search_left()
        right = 0
        if left == n or nums[left] != target:
            return [-1, -1]
        for i in range(left, n):
            if nums[i] == target:
                right = i
        return [left, right]


class Solution3:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left() -> int:
            low, high = 0, n
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        n = len(nums)
        left = binary_search_left()
        right = left
        if left == n or nums[left] != target:
            return[-1, -1]
        for i in range(left + 1, n):
            if nums[i] == target:
                right = i
        return [left, right]


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2, 2, 2]
    target = 2
    s = Solution3()
    print(s.searchRange(nums, target))
