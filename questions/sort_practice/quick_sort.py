# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: quick_sort
@time: 2021/12/6 6:27 下午
@desc: 
"""
import datetime
from typing import List
import random


def generate_random_array(n):
    nums = list(range(n))
    random.shuffle(nums)
    print(nums)
    return nums


class QuickSort:
    """
    不稳定 时间复杂度在最坏情况下是O(N2)，平均的时间复杂度是O(N*lgN)
    """

    def quick_sort(self, nums: List[int]) -> List[int]:
        if len(nums) >= 2:
            mid = nums[len(nums) // 2]
            left, right = [], []
            nums.remove(mid)
            for num in nums:
                if num >= mid:
                    right.append(num)
                else:
                    left.append(num)
            return self.quick_sort(left) + [mid] + self.quick_sort(right)
        else:
            return nums

    def quick_sort2(self, nums: List[int]) -> List[int]:
        def qsort(nums: List[int], l: int, r: int):
            if l < r:
                i, j = l, r
                x = nums[i]
                while i < j:
                    # 从右向左找第一个小于x的数
                    while i < j and nums[j] > x:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1
                    # 从左向右找第一个大于x的数
                    while i < j and nums[i] < x:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1
                nums[i] = x
                qsort(nums, l, i - 1)
                qsort(nums, i + 1, r)

        qsort(nums, 0, len(nums) - 1)
        return nums


class QuickSort2:
    """
    不稳定 时间复杂度在最坏情况下是O(N2)，平均的时间复杂度是O(N*lgN)
    """

    def quick_sort(self, nums: List[int]) -> List[int]:
        self._quick_sort2(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort1(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        i = l - 1
        j = r + 1
        x = nums[(l + r) >> 1]
        while i < j:
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        self._quick_sort1(nums, l, j)
        self._quick_sort1(nums, j + 1, r)

    def _quick_sort2(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        i = l - 1
        j = r + 1
        x = nums[(i + j) >> 1]
        print(x)
        while i < j:
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        self._quick_sort2(nums, l, j)
        self._quick_sort2(nums, j + 1, r)


class QuickSort3:
    """
    不稳定 时间复杂度在最坏情况下是O(N2)，平均的时间复杂度是O(N*lgN)
    """

    def quick_sort(self, nums: List[int]) -> List[int]:
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums: List[int], l: int, r: int) -> None:
        if l >= r:
            return
        i, j = l - 1, r + 1
        x = nums[i + j >> 1]
        while i < j:
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        self._quick_sort(nums, l, j)
        self._quick_sort(nums, j + 1, r)


class QuickSort4:

    def quick_sort(self, nums):
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums, l, r):
        # 1.递归终止条件
        if l >= r:
            return
        # 2.
        i, j = l - 1, r + 1
        # 3.
        x = nums[i + j >> 1]
        while i < j:
            # 4.
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            # 5.
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        # 6.
        self._quick_sort(nums, l, j)
        self._quick_sort(nums, j + 1, r)


class QuickSort5:

    def quick_sort(self, nums):
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums, l, r):
        if l >= r:
            return
        i, j = l - 1, r + 1
        x = nums[i + j >> 1]
        while i < j:
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        self._quick_sort(nums, l, j)
        self._quick_sort(nums, j + 1, r)


class QuickSort6:

    def quick_sort(self, nums):
        self._quick_sort(nums, 0, len(nums) - 1)

    def _quick_sort(self, nums, l, r):
        if l >= r:
            return

        i, j = l - 1, r + 1
        x = nums[l + r >> 1]
        while i < j:
            i += 1
            while nums[i] < x:
                i += 1
            j -= 1
            while nums[j] > x:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        self._quick_sort(nums, l, j)
        self._quick_sort(nums, j + 1, r)


if __name__ == '__main__':
    nums = generate_random_array(100)
    qsort = QuickSort6()
    time1 = datetime.datetime.now()
    qsort.quick_sort(nums)
    print(nums)
    time2 = datetime.datetime.now()
    print(time2 - time1)
