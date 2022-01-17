# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1_most_words
@time: 2021/12/25 10:30 下午
@desc: 
"""
from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sen in sentences:
            l = len(sen.split(" "))
            ans = max(l, ans)
        return ans
