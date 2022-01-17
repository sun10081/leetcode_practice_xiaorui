# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 704_search
@time: 2021/12/12 11:42 下午
@desc: 
"""
from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect(nums, target) - 1
        return idx if nums[idx] == target else -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect(nums, target) - 1
        return idx if nums[idx] == target else - 1

    def search3(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else - 1


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        # search_right
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left - 1 if nums[left] == target else -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    # print(bisect.bisect(nums, target))
    # print(bisect.bisect_left(nums, target))
    # ans = bisect.bisect(nums, target)
    # print(ans)
    s = Solution3()
    print(s.search(nums, target))
