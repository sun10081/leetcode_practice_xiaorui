# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 275_h_index_ii.py
@time: 2023-10-30 09:28:45 
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for _, c in enumerate(reversed(citations)):
            if c > h:
                h += 1
        return h

    def hIndex2(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = l + r >> 1
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid
        return n - l


if __name__ == '__main__':
    s = Solution()
    citations = [0, 1, 3, 5, 6]
    print(s.hIndex2(citations))