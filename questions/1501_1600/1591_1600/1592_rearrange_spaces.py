# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1592_rearrange_spaces.py
@time: 2022-09-07 12:50:57 
"""
from typing import List

SPACE_STR = ' '


class Solution:

    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(SPACE_STR)
        words = text.split()
        if len(words) == 1:
            return words[0] + SPACE_STR * space_count
        avg_space, last_space = divmod(space_count, len(words) - 1)
        return (SPACE_STR * avg_space).join(words) + SPACE_STR * last_space


if __name__ == '__main__':
    text = 'a'
    s = Solution()
    print(s.reorderSpaces(text))
