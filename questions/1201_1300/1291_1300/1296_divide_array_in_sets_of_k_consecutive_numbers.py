# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1296_divide_array_in_sets_of_k_consecutive_numbers
@time: 2021/12/31 10:07 上午
@desc: 
"""
from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        nums.sort()
        count = Counter(nums)
        for num in nums:
            if count[num] == 0:
                continue
            for next_num in range(num, num + k):
                if count[next_num] == 0:
                    return False
                count[next_num] -= 1
        return True

