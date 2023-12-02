# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 253_meeting_rooms_ii.py
@time: 2023-11-02 21:12:00 
"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        for interval in intervals:
            if not ans:
                heapq.heappush(ans, interval[1])
            else:
                cur = heapq.heappop(ans)
                if cur > interval[0]:
                    heapq.heappush(ans, cur)
                heapq.heappush(ans, interval[1])
        return len(ans)


if __name__ == '__main__':
    intervals = [[6, 15], [13, 20], [6, 17]]
    s = Solution()
    print(s.minMeetingRooms(intervals))
