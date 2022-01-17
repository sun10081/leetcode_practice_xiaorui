# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 136_single_number
@time: 2021/11/30 7:38 下午
@desc: 
"""
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    s = Solution2()
    print(s.singleNumber2(nums))
