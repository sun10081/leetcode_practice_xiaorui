# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1_checkString
@time: 2022/1/2 10:30 上午
@desc: 
"""


class Solution:
    def checkString(self, s: str) -> bool:
        flag = True
        for ch in s:
            if ch == 'b':
                flag = False
            if not flag and ch == 'a':
                return False
        return True
