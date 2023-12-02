# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1750_minimum_length.py
@time: 2022-12-28 09:25:46 
"""
from typing import List


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while r >= l and s[r] == ch:
                r -= 1
        return r - l + 1


if __name__ == '__main__':
    s = "bbbbbbbbbbbbbbbbbbb"
    so = Solution()
    print(so.minimumLength(s))
