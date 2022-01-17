# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2_add_spaces
@time: 2021/12/19 11:00 上午
@desc: 
"""
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_array = []
        point = 0
        for i in range(len(s)):
            if point < len(spaces) and i == spaces[point]:
                s_array.append(" ")
                point += 1
            s_array.append(s[i])
        return "".join(s_array)


if __name__ == '__main__':
    s = "LeetcodeHelpsMeLearn"
    spaces = [8, 13, 15]
    so = Solution()
    print(so.addSpaces(s, spaces))
