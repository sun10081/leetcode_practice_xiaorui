# coding=utf-8

from typing import List


class Solution:
    def checkSubarraySum(self, nums, k):
        d = {0: -1}
        pre = 0
        for index, num in enumerate(nums):
            pre += num
            rem = pre % k
            i = d.get(rem, index)
            if i == index:
                d[rem] = index
            elif i <= index - 2:
                return True
            return False
