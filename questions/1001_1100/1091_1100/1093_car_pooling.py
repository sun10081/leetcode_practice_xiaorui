# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1093_car_pooling.py
@time: 2023-12-02 09:07:14 
"""
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[0], x[2]))
        distance = [0] * 1001
        cur = 0
        for t, st, end in trips:
            cur = max(cur, st)
            for i in range(st, end):
                distance[i] += t
                if distance[i] > capacity:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3
    print(s.carPooling(trips, capacity))
