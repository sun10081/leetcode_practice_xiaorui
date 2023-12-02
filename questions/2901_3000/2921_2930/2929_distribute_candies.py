# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2929_distribute_candies.py
@time: 2023-11-13 16:34:51 
"""
import math
from typing import List


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        i_start = max(0, n - 2 * limit)
        i_end = min(limit, n)
        for i in range(i_start, i_end + 1):
            j_start = max(0, n - i - limit)
            j_end = min(limit, n - i)
            ans += j_end + 1 - j_start
        return ans

    def distributeCandies2(self, n: int, limit: int) -> int:
        total = math.comb(n + 2, n)
        c1 = math.comb(n + 2 - (limit + 1), 2)
        c2 = math.comb(n + 2 - 2 * (limit + 1), 2)
        c3 = math.comb(n + 2 - 3 * (limit + 1), 2)
        return total + 3 * c1 - 3 * c2 + c3


class Solution2:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = math.comb(n + 2, n)
        c1 = 3 * math.comb(n + 2 - (limit + 1), 2) if n + 2 - (limit + 1) > 1 else 0
        c2 = 3 * math.comb(n + 2 - 2 * (limit + 1), 2) if n + 2 - 2 * (limit + 1) > 1 else 0
        c3 = math.comb(n + 2 - 3 * (limit + 1), 2) if n + 2 - 3 * (limit + 1) > 1 else 0
        return total - c1 + c2 - c3


if __name__ == '__main__':
    s = Solution()
    n = 10001
    limit = 20001
    print(s.distributeCandies(n, limit))
    print(math.comb(4, 3))