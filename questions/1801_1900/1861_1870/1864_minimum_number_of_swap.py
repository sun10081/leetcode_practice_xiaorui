# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1864_minimum_number_of_swap.py
@time: 2023-11-10 00:49:21
"""
from math import inf
from typing import List


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        one_cnt = s.count('1')
        if abs(one_cnt - (n - one_cnt)) >= 2:
            return -1

        # 奇数 1
        one_cnt1, zero_cnt1 = 0, 0
        for i in range(n):
            if i % 2 == 0 and s[i] != '0':
                zero_cnt1 += 1
            if i % 2 and s[i] != '1':
                one_cnt1 += 1
        cnt1 = one_cnt1 if one_cnt1 == zero_cnt1 else inf
        # 偶数1
        one_cnt2, zero_cnt2 = 0, 0
        for i in range(n):
            if i % 2 == 0 and s[i] != '1':
                one_cnt2 += 1
            if i % 2 and s[i] != '0':
                zero_cnt2 += 1
        cnt2 = one_cnt2 if one_cnt2 == zero_cnt2 else inf
        return min(cnt1, cnt2)

    def minSwaps2(self, s: str) -> int:
        n = len(s)
        one_cnt = s.count('1')
        if abs(one_cnt - (n - one_cnt)) >= 2:
            return -1
        # 10101
        zero_cnt1, one_cnt1 = 0, 0
        for i in range(n):
            if not i % 2 and s[i] != '1':
                zero_cnt1 += 1
            if i % 2 and s[i] != '0':
                one_cnt1 += 1
        cnt1 = one_cnt1 if one_cnt1 == zero_cnt1 else inf
        # 01010
        zero_cnt2, one_cnt2 = 0, 0
        for i in range(n):
            if not i % 2 and s[i] != '0':
                one_cnt2 += 1
            if i % 2 and s[i] != '1':
                zero_cnt2 += 1
        cnt2 = one_cnt2 if one_cnt2 == zero_cnt2 else inf
        return min(cnt1, cnt2)


if __name__ == '__main__':
    so = Solution()
    s = "111000"
    print(so.minSwaps2(s))
