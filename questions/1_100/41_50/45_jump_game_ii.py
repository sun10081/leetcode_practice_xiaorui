# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 45_jump_game_ii.py
@time: 2023-08-09 10:05:39 
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cur_distance = 0
        step = 0
        end = 0

        for i in range(n - 1):
            if cur_distance >= i:
                cur_distance = max(cur_distance, i + nums[i])

                if i == end:
                    end = cur_distance
                    step += 1
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.jump(nums))