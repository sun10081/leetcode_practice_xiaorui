# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1663_smallest_string.py
@time: 2023-01-26 08:29:18 
"""
from typing import List
import string


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for i in range(1, n + 1):
            lower = max(1, k - (n - i) * 26)
            k -= lower
            ans.append(string.ascii_lowercase[lower - 1])
        return "".join(ans)


if __name__ == '__main__':
    n = 3
    k = 27
    s = Solution()
    print(s.getSmallestString(n, k))
