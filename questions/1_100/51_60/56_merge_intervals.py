# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 56_merge_intervals
@time: 2021/12/15 12:35 上午
@desc: 
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


class Solution4:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        for interval in intervals:
            if not ans:
                ans.append(interval)
            else:
                if interval[0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], interval[1])
                else:
                    ans.append(interval)
        return ans


if __name__ == '__main__':
    intervals = [[1, 4], [2, 3], [1, 3]]
    s = Solution4()
    print(s.merge(intervals))
