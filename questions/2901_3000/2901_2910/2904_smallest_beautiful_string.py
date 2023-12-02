# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2904_smallest_beautiful_string.py
@time: 2023-10-17 21:37:29 
"""
from typing import List


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        ans = s
        one_count = 0
        j = 0
        for i in range(len(s)):
            one_count += int(s[i])
            while one_count > k or s[j] == '0':
                one_count -= int(s[j])
                j += 1
            if one_count == k:
                t = s[j: i + 1]
                if len(t) < len(ans) or len(t) == len(ans) and ans > t:
                    ans = t
        return ans


class Solution2:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''

        one_count, i = 0, 0
        n = len(s)
        ans = s
        for j in range(n):
            one_count += int(s[j])
            while s[i] == '0' or one_count > k:
                one_count -= int(s[i])
                i += 1
            if one_count == k:
                t = s[i: j + 1]
                if len(t) < len(ans) or len(t) == len(ans) and ans > t:
                    ans = t
        return ans


if __name__ == '__main__':
    so = Solution2()
    s = "100011001"
    k = 3
    print(so.shortestBeautifulSubstring(s, k))



