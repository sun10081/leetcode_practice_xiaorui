# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1624_largest_substring.py
@time: 2022-09-17 23:39:21 
"""
from typing import List
from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        len_count = defaultdict(int)
        ans = -1
        for index, ch in enumerate(s):
            if ch in len_count:
                ans = max(ans, index - len_count[ch])
            else:
                len_count[ch] = index
        return ans - 1 if ans != -1 else -1


if __name__ == '__main__':
    so = Solution()
    s = "mgntdygtxrvxjnwksqhxuxtrv"
    print(so.maxLengthBetweenEqualCharacters(s))

