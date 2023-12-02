# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2336_smallest_numbe.py
@time: 2023-11-29 12:02:10 
"""
from sortedcontainers import SortedSet


class SmallestInfiniteSet:

    def __init__(self):
        self.start = 1
        self.s = SortedSet()

    def popSmallest(self) -> int:
        if not self.s:
            ans = self.start
            self.start += 1
            return ans

        return self.s.pop(0)

    def addBack(self, num: int) -> None:
        if num < self.start:
            self.s.add(num)

