# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2103_rings_and_rod
@time: 2021/12/25 10:01 下午
@desc: 
"""
from typing import List


class Solution:
    def countPoints(self, rings: str) -> int:
        counts = [0] * 10
        n = len(rings)
        # 'R'、'G'、'B'
        for i in range(0, n - 1, 2):
            index = int(rings[i + 1])
            if rings[i] == "R":
                counts[index] |= 1
            elif rings[i] == "G":
                counts[index] |= 2
            elif rings[i] == "B":
                counts[index] |= 4
        ans = 0
        for i in range(10):
            if counts[i] == 7:
                ans += 1
        return ans


