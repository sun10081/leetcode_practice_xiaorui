# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2562_sum_multiples.py
@time: 2023-10-17 03:04:43 
"""
from typing import List


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                ans += i
        return ans


class Solution2:
    def sumOfMultiples(self, n: int) -> int:
        def f(m: int) -> int:
            return (m + n // m * m) * (n // m) // 2
        return f(3) + f(5) + f(7) - f(3 * 5) - f(3 * 7) - f(5 * 7) + f(3 * 5 * 7)


if __name__ == '__main__':
    s = Solution2()
    n = 7
    print(s.sumOfMultiples(n))