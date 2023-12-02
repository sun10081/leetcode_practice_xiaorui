# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1768_merge_strings_alternately.py
@time: 2022-10-23 23:16:15 
"""
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_str = []
        for x, y in zip_longest(word1, word2, fillvalue=None):
            if x:
                merge_str.append(x)
            if y:
                merge_str.append(y)
        return "".join(merge_str)


if __name__ == '__main__':
    word1 = "ab"
    word2 = "pqrs"
    s = Solution()
    print(s.mergeAlternately(word1, word2))