# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/9/10 10:35 AM
@desc:
"""
from typing import List


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        abs_y = abs(fy - sy)
        abs_x = abs(fx - sx)
        min_t = 0
        if sx == fx and sy == fy:
            return t != 1
        elif sx == fx or sy == fy:
            min_t = max(abs(sx - fx), abs(sy - fy))
        else:
            min_t = min(abs_x, abs_y)
            min_t += max(abs_x, abs_y) - min(abs_x, abs_y)
        return t >= min_t


if __name__ == '__main__':
    s = Solution()
    sx = 1
    sy = 2
    fx = 1
    fy = 2
    t = 1
    print(s.isReachableAtTime(sx, sy, fx, fy, t))