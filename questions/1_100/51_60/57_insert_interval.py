# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 57_insert_interval.py
@time: 2023-08-28 14:17:47 
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        if not intervals:
            return [newInterval]

        has_insert = False
        nl, nr = newInterval
        for l, r in intervals:
            if l > nr:
                if not has_insert:
                    ans.append([nl, nr])
                    has_insert = True
                ans.append([l, r])
            elif r < nl:
                ans.append([l, r])
            else:
                nl = min(nl, l)
                nr = max(nr, r)
        if not has_insert:
            ans.append([nl, nr])
        return ans


if __name__ == '__main__':
    intervals = [[1, 5]]
    newInterval = [2, 3]
    s = Solution()
    print(s.insert(intervals, newInterval))
