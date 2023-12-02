# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2023_9_25
@time: 2023/9/25 10:56 AM
@desc:
"""
from typing import Tuple


class Solution:

    def find_ch(self, target_str: str) -> Tuple:
        ch_list = [0] * 26

        for ch in target_str:
            ch_list[ord(ch) - ord('a')] += 1

        ans_times = 0
        ans = 'a'
        for i in range(26):
            if ch_list[i] > ans_times:
                ans = chr(i + ord('a'))
                ans_times = ch_list[i]
        return ans, ans_times


if __name__ == '__main__':
    s = Solution()
    target_str = 'abcdaaa'
    print(s.find_ch(target_str))
