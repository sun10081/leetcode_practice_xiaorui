# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2105_watering_plants
@time: 2021/12/25 10:16 下午
@desc: 
"""
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        point_a, point_b = 0, n - 1
        cur_capacity_a, cur_capacity_b = capacityA, capacityB
        ans = 0

        while point_a < point_b:
            if cur_capacity_a >= plants[point_a]:
                cur_capacity_a -= plants[point_a]
            else:
                cur_capacity_a = capacityA - plants[point_a]
                ans += 1

            if cur_capacity_b >= plants[point_b]:
                cur_capacity_b -= plants[point_b]
            else:
                cur_capacity_b = capacityB - plants[point_b]
                ans += 1
            point_a += 1
            point_b -= 1

        if point_a == point_b:
            if cur_capacity_a >= cur_capacity_b:
                if cur_capacity_a < plants[point_a]:
                    ans += 1
            else:
                if cur_capacity_b < plants[point_a]:
                    ans += 1
        return ans
