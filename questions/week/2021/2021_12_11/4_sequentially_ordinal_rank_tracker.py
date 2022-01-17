# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 4_sequentially_ordinal_rank_tracker
@time: 2021/12/12 2:06 上午
@desc: 
"""
import bisect
from sortedcontainers import SortedList


class SORTracker:

    def __init__(self):
        self.q, self.idx = [], 0

    def add(self, name: str, score: int) -> None:
        bisect.insort(self.q, (-score, name))
        print(self.q)

    def get(self) -> str:
        self.idx += 1
        print(self.q[self.idx - 1][1])
        return self.q[self.idx - 1][1]


class SORTracker2:

    def __init__(self):
        self.data = SortedList([])
        self.cnt = 0

    def add(self, name: str, score: int) -> None:
        self.data.add((-score, name))

    def get(self) -> str:
        self.cnt += 1
        return self.data[self.cnt - 1][1]


if __name__ == '__main__':
    tracker = SORTracker()
    tracker.add("bradford", 2)
    tracker.add("branford", 3)
    tracker.get()
    tracker.add("alps", 2)
    tracker.get()
    tracker.add("orland", 2)
    tracker.get()



