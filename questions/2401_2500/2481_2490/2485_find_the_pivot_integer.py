# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2485_find_the_pivot_integer.py
@time: 2023-06-26 10:22:45 
"""
from typing import List


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n * n + n) // 2
        x = int(total ** 0.5)
        if x * x == total:
            return x
        return - 1
