# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 849_maximize_distance.py
@time: 2023-08-22 11:30:01 
"""
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        start, end = None, None
        distance = 0

        for i in range(n):
            if seats[i]:
                if end is not None:
                    distance = max(distance, i - end)
                if start is None:
                    start = i
                end = i

        ans = max(distance // 2, start, n - 1 - end)
        return ans


if __name__ == '__main__':
    s = Solution()
    seats = [1, 0, 0, 0, 1, 0, 1]
    print(s.maxDistToClosest(seats))
