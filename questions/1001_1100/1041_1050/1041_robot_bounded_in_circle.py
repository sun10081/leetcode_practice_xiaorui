# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1041_robot_bounded_in_circle.py
@time: 2023-04-11 19:45:49 
"""
from typing import List


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [0] * 4
        k = 0
        for ch in instructions:
            if ch == "L":
                k = (k + 1) % 4
            elif ch == "r":
                k = (k + 3) % 4
            else:
                directions[k] += 1
        return (directions[0] == directions[2] and directions[1] == directions[3]) or k != 0
