# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 713_subarray_product_less_than_k.py
@time: 2023-10-30 23:24:00 
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1:
            return 0
        product = 1
        ans = 0
        l = 0

        for r in range(n):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            ans += r - l + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))
