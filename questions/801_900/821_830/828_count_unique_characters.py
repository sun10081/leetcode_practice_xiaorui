# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 828_count_unique_characters.py
@time: 2022-09-06 12:46:54 
"""
from typing import List
from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 遍历一遍
        ch_index = defaultdict(list)
        for index, ch in enumerate(s):
            ch_index[ch].append(index)

        ans = 0
        for arr in ch_index.values():
            # 考虑首尾
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return ans

