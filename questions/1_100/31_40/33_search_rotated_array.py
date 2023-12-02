# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 33_search_rotated_array
@time: 2021/11/30 4:57 下午
@desc: 
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        # 4 5 6 1 2 3
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1

        if target < nums[0]:
            r = n - 1
        else:
            l = 0

        while l < r:
            mid = l + r >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1

        if target < nums[0]:
            r = n - 1
        else:
            l = 0

        while l < r:
            mid = l + r >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1


class Solution4:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return end < target <= nums[i]
            else:
                return target > end or target <= nums[i]

        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = l + r >> 1
            if is_blue(mid):
                r = mid
            else:
                l = mid + 1
        if l == n or nums[l] != target:
            return -1
        return l


if __name__ == '__main__':
    nums = [1, 3]
    target = 3
    s = Solution4()
    print(s.search(nums, target))
