# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/8/27 10:29 AM
@desc:
"""
from typing import List


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lc, rc, tmp = 0, 0, 0
        for move in moves:
            if move == "L":
                lc += 1
            elif move == "R":
                rc += 1
            else:
                tmp += 1
        return tmp + abs(lc - rc)



