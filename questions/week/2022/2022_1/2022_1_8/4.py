# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 4
@time: 2022/1/8 10:16 下午
@desc: 
"""

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_arr = title.split(" ")
        for i in range(len(title_arr)):
            if len(title_arr[i]) >= 3:
                title_arr[i] = title_arr[i][0].upper() + title_arr[i][1:].lower()
            else:
                title_arr[i] = title_arr[i].lower()
        return " ".join(title_arr)
