# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2399_check_distances_between_same_letters.py
@time: 2023-04-09 11:17:19 
"""
from typing import List
from collections import defaultdict


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        count = defaultdict()
        for i, ch in enumerate(s):
            if count[ch] and i - count[ch] - 1 != distance[ord(ch) - ord('a')]:
                return False
            count[ch] = i
        return True
