# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 973_k_closest_points_to_origin.py
@time: 2022-01-17 01:40:07 
"""
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def quick_select(l: int, r: int, k: int) -> int:
            if l == r:
                return l
            i, j = l - 1, r + 1
            x = points[random.randint(l, r)][0]
            while i < j:
                i += 1
                while points[i][0] < x:
                    i += 1
                j -= 1
                while points[j][0] > x:
                    j -= 1
                if i < j:
                    points[i], points[j] = points[j], points[i]
            sl = j - l + 1
            if k <= sl:
                return quick_select(l, j, k)
            return quick_select(j + 1, r, k - sl)

        points = [[p[0] * p[0] + p[1] * p[1], p[0], p[1]] for p in points]
        index = quick_select(0, len(points) - 1, K)
        ans = [[p[1], p[2]] for p in points[:K]]
        return ans


if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    K = 1
    s = Solution()
    print(s.kClosest(points, K))
    print(points)
