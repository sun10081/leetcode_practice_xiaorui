# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 739_daily_temperatures.py
@time: 2023-11-02 19:51:41 
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i, t in enumerate(temperatures):
            t = temperatures[i]
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

