# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 55_jump_game.py
@time: 2023-07-28 02:06:31 
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cur_longest_distance = 0
        for i in range(n):
            if i <= cur_longest_distance:
                cur_longest_distance = max(cur_longest_distance, i + nums[i])
                if cur_longest_distance >= n - 1:
                    return True
        return False

