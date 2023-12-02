# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2530_maximal_score.py
@time: 2023-10-18 09:59:35 
"""
import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        ans = 0

        while k:
            ans -= heapq.heapreplace(nums, nums[0] // 3)
            k -= 1
        return ans


class Solution2:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while k:
            ans -= heapq.heapreplace(nums, nums[0] // 3)
            k -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 10, 3, 3, 3]
    k = 3
    print(s.maxKelements(nums, k))
