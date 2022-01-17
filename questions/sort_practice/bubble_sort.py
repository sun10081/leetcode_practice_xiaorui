# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: bubble_sort
@time: 2021/12/6 6:11 下午
@desc: 
"""
import datetime
from typing import List


class BubbleSort:
    """
    稳定的排序算法 时间复杂度是O(N2)
    """
    def bubble_sort(self, nums: List[int]):
        n = len(nums)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def bubble_sort_improvement(self, nums: List[int]):
        n = len(nums)
        for i in range(n - 1, 0, -1):
            flag = True
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = False
            if flag:
                break
        return nums


if __name__ == '__main__':
    nums = [5, 1, 7, 4, 8, 9, 6, 3, 10, 2]
    bubble = BubbleSort()
    time1 = datetime.datetime.now()
    print(bubble.bubble_sort(nums))
    time2 = datetime.datetime.now()
    print(time2 - time1)