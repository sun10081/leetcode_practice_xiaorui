# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 76_minimum_window_substring.py
@time: 2023-11-24 10:17:25 
"""
from typing import List
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        c1 = Counter(t)
        c2 = Counter()
        ans = ""
        l, n = 0, len(s)
        for r in range(n):
            if s[r] in c2:
                c2[s[r]] += 1
            else:
                c2.update({s[r]: 1})

            while l <= r and c1 & c2 == c1:
                if not ans:
                    ans = s
                ans = self.min_str(ans, s[l: r + 1])
                c2[s[l]] -= 1
                l += 1
        return ans

    def min_str(self, s1, s2):
        m, n = len(s1), len(s2)
        if m < n:
            return s1
        elif m > n:
            return s2
        return min(s1, s2)


if __name__ == '__main__':
    so = Solution()
    s = "a"
    t = "a"
    print(so.minWindow(s, t))
