# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1465_maximum_area.py
@time: 2023-10-27 10:10:28 
"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10 ** 9 + 7
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)

        max_h = 0
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])
        max_w = 0
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])
        return max_h * max_w % mod