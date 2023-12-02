# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2698_find_the_punishment_number.py
@time: 2023-10-26 10:14:54 
"""
from typing import List


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s: str, pos: int, total: int, target: int) -> bool:
            if pos == len(s):
                return total == target
            cur_sum = 0
            for i in range(pos, len(s)):
                cur_sum = cur_sum * 10 + int(s[i])
                if cur_sum + total > target:
                    break
                if dfs(s, i + 1, total + cur_sum, target):
                    return True
                
            return False

        ans = 0
        for i in range(1, n + 1):
            if dfs(str(i * i), 0, 0, i):
                ans += i * i
        return ans

