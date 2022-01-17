# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3_asteroidsDestroyed
@time: 2022/1/2 10:43 上午
@desc: 
"""
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        ans = mass
        for i in range(len(asteroids)):
            if ans >= asteroids[i]:
                ans += asteroids[i]
            else:
                return False
        return True
