# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2309_greatest_english_letter.py
@time: 2023-01-27 09:01:21 
"""
from typing import List


class Solution:
    def greatestLetter(self, s: str) -> str:
        lower = [0] * 26
        upper = [0] * 26
        for ch in s:
            if ch.islower():
                lower[ord(ch) - ord("a")] = 1
            else:
                upper[ord(ch) - ord("A")] = 1
        for i in range(25, -1, -1):
            if lower[i] and upper[i]:
                return chr(ord("A") + i)
        return ""


if __name__ == '__main__':
    so = Solution()
    s = "arRAzFif"
    print(so.greatestLetter(s))
