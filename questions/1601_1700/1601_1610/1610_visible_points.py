# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1610_visible_points
@time: 2021/12/16 10:09 上午
@desc: 
"""
import bisect
from math import atan2, pi
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # 每个元素 +2*pi的意义
        # 二分查找 -i的意义
        same_count, max_count = 0, 0
        polar_degrees = []
        for point in points:
            # 统计坐标刚好位于起点的待观察点
            if point == location:
                same_count += 1
            # 通过反正切 求出待观察点的极角度数
            else:
                polar_degrees.append(atan2(point[1] - location[1], point[0] - location[0]))
        polar_degrees.sort()

        n = len(polar_degrees)
        for degree in polar_degrees:
            polar_degrees.append(degree + 2 * pi)

        degree = angle * pi / 180
        for i in range(n):
            max_count = max(max_count, bisect.bisect(polar_degrees, polar_degrees[i] + degree) - i)
        return same_count + max_count


if __name__ == '__main__':
    points = [[1, 1], [1, 1], [1, 1]]
    angle = 1
    location = [1, 1]
    s = Solution()
    print(s.visiblePoints(points, angle, location))
