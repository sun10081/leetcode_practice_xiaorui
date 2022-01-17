# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1_first_palindrome
@time: 2021/12/19 10:58 上午
@desc: 
"""
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
