# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2825_make_string.py
@time: 2023-08-21 22:05:32 
"""
from typing import List


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False

        i = 0
        for ch1 in str1:
            ch2 = chr(ord(ch1) + 1) if ch1 != 'z' else 'a'
            if ch1 == str2[i] or ch2 == str2[i]:
                i += 1
                if i == len(str2):
                    return True
        return False