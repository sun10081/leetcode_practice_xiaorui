# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2351_first_letter_to_appear_twice.py
@time: 2023-01-01 08:43:47 
"""
from typing import List


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ch_list = [0] * 26
        for ch in s:
            ch_ord = ord(ch) - ord('a')
            if ch_list[ch_ord] == 1:
                return ch
            ch_list[ch_ord] += 1



