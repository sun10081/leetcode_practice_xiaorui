# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1726_tuple_with_same_product.py
@time: 2023-10-19 14:32:37 
"""
from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                count[nums[i] * nums[j]] += 1
        for _, value in count.items():
            ans += value * (value - 1) * 4
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 4, 6]
    print(s.tupleSameProduct(nums))

