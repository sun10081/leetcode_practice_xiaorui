# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2930_number_of_strings.py
@time: 2023-11-13 17:03:06 
"""
import math
from functools import lru_cache


class Solution:
    def stringCount(self, n: int) -> int:
        @lru_cache
        def dfs(i: int, l: int, t: int, e: int) -> int:
            if i == 0:
                return 1 if l == t == e == 0 else 0
            res = dfs(i - 1, 0, t, e)
            res += dfs(i - 1, l, 0, e)
            res += dfs(i - 1, l, t, max(e - 1, 0))
            res += dfs(i - 1, l, t, e) * 23
            return res % (10 ** 9 + 7)

        return dfs(n, 1, 1, 2)

    def stringCount2(self, n: int) -> int:
        mod = 10 ** 9 + 7
        total1 = math.pow(26, n) % mod
        total2 = pow(26, n, mod)
        print(f"total1={total1}, total2={total2}")
        # 不包含l或者t或者e + 只包含1个e的情况
        c11 = (math.pow(25, n - 1) % mod) * (75 + n)
        c12 = pow(25, n - 1, mod) * (75 + n)
        print(f"c1={c11}, c2={c12}")
        # 不含l和t, 不含l和e， 不含t和e， 1个e+不含l或t
        c21 = (72 + 2 * n) * (math.pow(24, n - 1) % mod)
        c22 = pow(24, n - 1, mod) * (72 + 2 * n)
        print(f"c21={c21}, c22={c22}")
        # 3个都不包含 或者只包含1个e
        c31 = (23 + n) * (math.pow(23, n - 1) % mod)
        c32 = pow(23, n - 1, mod) * (23 + n)
        print(f"c31={c31}, c32={c32}")
        ans1 = (total1 - c11 + c21 - c31) % mod
        ans2 = (total2 - c12 + c22 - c32) % mod
        print(f"ans1={ans1}, ans2={ans2}")
        return int(ans1)

    def stringCount3(self, n: int) -> int:
        mod = 10 ** 9 + 7
        total = pow(26, n, mod)
        # 不包含l或者t或者e + 只包含1个e的情况
        c1 = pow(25, n - 1, mod) * (75 + n)
        # 不含l和t, 不含l和e， 不含t和e， 1个e+不含l或t
        c2 = pow(24, n - 1, mod) * (72 + 2 * n)
        # 3个都不包含 或者只包含1个e
        c3 = pow(23, n - 1, mod) * (23 + n)
        ans = (total - c1 + c2 - c3) % mod
        return int(ans)


class Solution2:
    def stringCount(self, n: int) -> int:
        @lru_cache
        def dfs(i, l, t, e):
            if i == 0:
                return 1 if l == t == e == 0 else 0

            res = dfs(i - 1, 0, t, e)
            res += dfs(i - 1, l, 0, e)
            res += dfs(i - 1, l, t, max(e - 1, 0))
            res += dfs(i - 1, l, t, e) * 23
            return res % (10 ** 9 + 7)

        return dfs(n, 1, 1, 2)


if __name__ == '__main__':
    s = Solution2()
    n = 10
    print(s.stringCount(n))
