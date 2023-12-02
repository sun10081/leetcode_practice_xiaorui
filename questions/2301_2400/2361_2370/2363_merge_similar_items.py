# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2363_merge_similar_items.py
@time: 2023-02-28 17:46:18 
"""
from typing import List
from collections import Counter


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = Counter()
        for k, v in items1:
            count[k] += v
        for k, v in items2:
            count[k] += v
        ans = sorted([a, b] for a, b in count.items())
        return ans