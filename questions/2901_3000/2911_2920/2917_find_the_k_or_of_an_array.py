# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2917_find_the_k_or_of_an_array.py
@time: 2023-11-03 00:59:11 
"""
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = 30
        ans = 0
        for i in range(cnt):
            tmp = sum(num >> i & 1 for num in nums)
            if tmp >= k:
                ans += 1 << i
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [7, 12, 9, 8, 9, 15]
    k = 4
    print(s.findKOr(nums, k))