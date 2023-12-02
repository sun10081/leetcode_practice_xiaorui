# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1790_swap_strings.py
@time: 2022-10-11 23:59:38 
"""
from typing import List


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        first_diff_index = -1
        diff_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff_count == 0:
                    first_diff_index = i
                    diff_count += 1
                elif s2[i] == s1[first_diff_index] and s2[first_diff_index] == s1[i]:
                    diff_count += 1
                else:
                    return False

        return diff_count == 2 or diff_count == 0


if __name__ == '__main__':
    s1 = "abcd"
    s2 = "dcba"
    s = Solution()
    print(s.areAlmostEqual(s1, s2))