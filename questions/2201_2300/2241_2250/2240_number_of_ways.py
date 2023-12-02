# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2240_number_of_ways.py
@time: 2023-09-01 17:24:26 
"""
from typing import List


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        cnt1 = total // cost1
        while cnt1 >= 0:
            ans += (total - cost1 * cnt1) // cost2 + 1
            cnt1 -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    total = 5
    cost1 = 10
    cost2 = 10
    print(s.waysToBuyPensPencils(total, cost1, cost2))

