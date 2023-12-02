# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1828_queries_on_number.py
@time: 2023-01-24 09:14:20 
"""
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            for point in points:
                if (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2 <= query[2] * query[2]:
                    ans[i] += 1
        return ans


if __name__ == '__main__':
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    s = Solution()
    print(s.countPoints(points, queries))
