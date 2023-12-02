# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2931_maximum_spending.py
@time: 2023-11-15 10:37:20 
"""
import heapq
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        ans = []
        for value in values:
            for i in value:
                heapq.heappush(ans, i)
        n, m = len(values), len(values[0])
        d = 1
        res = 0
        while d <= n * m:
            res += heapq.heappop(ans) * d
            d += 1
        return res


if __name__ == '__main__':
    s = Solution()
    values = [[8, 5, 2], [6, 4, 1], [9, 7, 3]]
    print(s.maxSpending(values))

