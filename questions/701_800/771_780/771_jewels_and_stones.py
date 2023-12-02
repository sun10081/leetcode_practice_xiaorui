# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 771_jewels_and_stones.py
@time: 2023-07-24 23:09:09 
"""
from typing import List
from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        count = defaultdict(int)
        for ch in jewels:
            count[ch] = 0
        for stone in stones:
            if stone in count:
                ans += 1
        return ans


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    s = Solution()
    print(s.numJewelsInStones(jewels, stones))
