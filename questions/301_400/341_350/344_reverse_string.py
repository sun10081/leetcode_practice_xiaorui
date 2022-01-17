# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 344_reverse_string
@time: 2021/12/17 12:29 上午
@desc: 
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
