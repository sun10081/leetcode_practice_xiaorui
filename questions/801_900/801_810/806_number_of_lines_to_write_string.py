# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 806_number_of_lines_to_write_string.py
@time: 2022-04-12 12:41:52 
"""
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cur_len = 0
        line_num = 1
        for ch in s:
            index = ord(ch) - ord('a')
            if cur_len + widths[index] > 100:
                line_num += 1
                cur_len = 0
            cur_len += widths[index]

        return [line_num, cur_len]


if __name__ == '__main__':
    s = Solution()
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print(s.numberOfLines(widths, S))
