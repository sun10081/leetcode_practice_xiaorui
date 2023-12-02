# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 822_card_flipping_game.py
@time: 2023-08-02 13:33:44 
"""
from typing import List
from collections import defaultdict


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = 2001
        forbid = defaultdict(int)
        n = len(fronts)
        for i in range(n):
            if fronts[i] == backs[i]:
                forbid[fronts[i]] = 1
        for i in range(n):
            if fronts[i] < ans and fronts[i] not in forbid:
                ans = fronts[i]
            if backs[i] < ans and backs[i] not in forbid:
                ans = backs[i]
        return ans if ans != 2001 else 0


if __name__ == '__main__':
    solution = Solution()
    fronts = [1]
    backs = [1]
    print(solution.flipgame(fronts, backs))
