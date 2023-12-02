# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1525_number_of_good_ways.py
@time: 2023-11-09 23:49:37 
"""
from typing import List
from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        c1 = Counter(s)
        n = len(s)
        c2 = Counter()
        ans = 0

        for i in range(n):
            c1[s[i]] -= 1
            if c1[s[i]] == 0:
                c1.pop(s[i])
            c2[s[i]] += 1
            if len(c1) == len(c2):
                ans += 1
        return ans


if __name__ == '__main__':
    s = "abcd"
    so = Solution()
    print(so.numSplits(s))