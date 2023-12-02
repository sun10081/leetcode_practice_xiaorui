# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1637_widest_vertical_area.py
@time: 2023-03-30 20:24:15 
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        ans = 0
        for i in range(1, len(points)):
            ans = max(ans, points[i][0] - points[i - 1][0])
        return ans


if __name__ == '__main__':
    s = Solution()
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(s.maxWidthOfVerticalArea(points))
