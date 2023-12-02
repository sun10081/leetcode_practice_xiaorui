# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1753_maximum_score_from_removing_stones.py
@time: 2022-12-21 09:39:07 
"""
from typing import List


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_val = max(a, b, c)
        stone_sum = sum([a, b, c])
        if max_val >= stone_sum / 2:
            return stone_sum - max_val
        return stone_sum // 2


if __name__ == '__main__':
    a = 1
    b = 8
    c = 8
    s = Solution()
    print(s.maximumScore(a, b, c))

