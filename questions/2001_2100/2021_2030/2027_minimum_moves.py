# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2027_minimum_moves.py
@time: 2022-12-27 10:23:05 
"""

from typing import List


class Solution:
    def minimumMoves(self, s: str) -> int:
        ans, covered = 0, -1
        for i, ch in enumerate(s):
            if ch == 'X' and i > covered:
                ans += 1
                covered = i + 2
        return ans


if __name__ == '__main__':
    s = "XXOX"
    so = Solution()
    print(so.minimumMoves(s))
