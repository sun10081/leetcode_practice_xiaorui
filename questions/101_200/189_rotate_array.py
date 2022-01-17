# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 189_rotate_array
@time: 2021/12/14 12:01 上午
@desc: 
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        # k 要对数组长度取余，轮转一趟相当于没转
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[: n - k]

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s = Solution3()
    s.rotate(nums, k)
    print(nums)
