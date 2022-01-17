# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 911_online_election
@time: 2021/12/11 11:59 上午
@desc: 
"""
import bisect
from typing import List
from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        vote_counts = defaultdict(int)
        vote_counts[-1] = -1
        top = -1
        for p in persons:
            vote_counts[p] = vote_counts.get(p, 0) + 1
            if vote_counts[p] >= vote_counts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.times[mid] == t:
                left = mid
                break
            elif self.times[mid] < t:
                left = mid
            else:
                right = mid - 1
        # left = bisect.bisect(self.times, t) - 1
        return self.tops[left]


class TopVotedCandidate2:
    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        vote_counts = defaultdict(int)
        vote_counts[-1] = -1
        top = -1
        for p in persons:
            vote_counts[p] = vote_counts.get(p, 0) + 1
            if vote_counts[p] >= vote_counts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        left = bisect.bisect(self.times, t) - 1
        return self.tops[left]


if __name__ == '__main__':
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    t = TopVotedCandidate2(persons, times)
    print(t.q(25))
