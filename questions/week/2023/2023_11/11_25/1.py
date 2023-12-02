# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/11/25 10:27 PM
@desc:
"""
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans