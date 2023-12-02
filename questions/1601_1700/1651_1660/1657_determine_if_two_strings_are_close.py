# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1657_determine_if_two_strings_are_close.py
@time: 2023-11-30 08:44:54 
"""
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())


if __name__ == '__main__':
    s = Solution()
    word1 = "abc"
    word2 = "bca"
    print(s.closeStrings(word1, word2))