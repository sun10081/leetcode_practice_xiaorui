# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 4
@time: 2022/1/16 10:40 下午
@desc: 
"""
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # 二分
        l, r = 0, sum(batteries) // n
        while l < r:
            x = (l + r + 1) // 2
            if n * x <= sum(min(b, x) for b in batteries):
                l = x
            else:
                r = x - 1
        return l
