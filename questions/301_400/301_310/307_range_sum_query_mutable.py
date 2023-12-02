# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 307_range_sum_query_mutable.py
@time: 2023-11-13 15:56:21 
"""
from typing import List
from itertools import accumulate


class NumArray:

    def __init__(self, nums: List[int]):
        # nums[i] = pre_sum[i + 1] - pre_sum[i]
        self.nums = nums
        self.pre_sum = [0] + list(accumulate(self.nums))

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        if diff:
            for i in range(index + 1, len(self.nums) + 1):
                self.pre_sum[i] += diff
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]


if __name__ == '__main__':
    nums = [7, 2, 7, 2, 0]
    n = NumArray(nums)
    n.update(4, 6)
    n.update(0, 2)
    n.update(0, 9)
    print(n.sumRange(4, 4))
    n.update(3, 8)
    print(n.sumRange(0, 4))
