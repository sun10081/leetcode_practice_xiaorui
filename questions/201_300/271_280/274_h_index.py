# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 274_h_index.py
@time: 2023-10-30 09:15:24 
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for c in citations:
            if c > h:
                h += 1
            else:
                break
        return h


if __name__ == '__main__':
    s = Solution()
    citations = [1, 3, 1]
    print(s.hIndex(citations))