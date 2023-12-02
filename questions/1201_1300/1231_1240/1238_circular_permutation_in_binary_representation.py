# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1238_circular_permutation_in_binary_representation.py
@time: 2023-02-23 15:06:26 
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i ^ start
        return ans
