# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 791_custom_sort_string.py
@time: 2022-11-13 23:54:49 
"""
from typing import List
from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sort_rule = defaultdict(int)
        for i, ch in enumerate(order):
            sort_rule[ch] = i + 1

        ans = sorted(s, key=lambda x: sort_rule[x])
        return "".join(ans)


if __name__ == '__main__':
    so = Solution()
    order = "cba"
    s = "abcd"
    print(so.customSortString(order, s))
