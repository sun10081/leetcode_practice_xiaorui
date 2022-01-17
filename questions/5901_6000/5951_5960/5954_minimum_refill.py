# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 5954_minimum_refill
@time: 2021/12/12 7:27 下午
@desc: 
"""
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        point_a, point_b = 0, len(plants) - 1
        current_capacity_a, current_capacity_b = capacityA, capacityB
        ans = 0
        while point_a < point_b:
            if current_capacity_a < plants[point_a]:
                current_capacity_a = capacityA - plants[point_a]
                ans += 1
            else:
                current_capacity_a -= plants[point_a]

            if current_capacity_b < plants[point_b]:
                current_capacity_b = capacityB - plants[point_b]
                ans += 1
            else:
                current_capacity_b -= plants[point_b]

            point_a += 1
            point_b -= 1

        if point_a == point_b:
            if current_capacity_a >= current_capacity_b:
                if current_capacity_a < plants[point_a]:
                    ans += 1
            else:
                if current_capacity_b < plants[point_a]:
                    ans += 1
        return ans


if __name__ == '__main__':
    plants = [2, 2, 5, 2, 2]
    capacityA = 5
    capacityB = 5
    s = Solution()
    print(s.minimumRefill(plants, capacityA, capacityB))


