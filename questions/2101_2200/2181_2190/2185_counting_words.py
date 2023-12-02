# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2185_counting_words.py
@time: 2023-01-08 08:54:23 
"""
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans += 1
        return ans


if __name__ == '__main__':
    words = ["pay", "attention", "practice", "attend"]
    pref = "at"
    s = Solution()
    print(s.prefixCount(words, pref))