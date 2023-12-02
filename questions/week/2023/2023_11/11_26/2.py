# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/11/26 10:29 AM
@desc:
"""
from typing import List


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        v_count = [0] * (n + 1)
        c_count = [0] * (n + 1)
        for i in range(1, n + 1):
            if s[i - 1] in ('a', 'e', 'i', 'o', 'u'):
                v_count[i] = v_count[i - 1] + 1
                c_count[i] = c_count[i - 1]
            else:
                v_count[i] = v_count[i - 1]
                c_count[i] = c_count[i - 1] + 1
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                v = v_count[j] - v_count[i]
                c = c_count[j] - c_count[i]
                if c == v and (c * v) % k == 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    so = Solution()
    s = "baeyh"
    k = 2
    print(so.beautifulSubstrings(s, k))

