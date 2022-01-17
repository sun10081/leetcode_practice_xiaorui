# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 630_schedule_course_two
@time: 2021/12/14 9:59 上午
@desc: 
"""
import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        total_time = 0
        time_queue = []
        courses.sort(key=lambda x: x[1])

        for time, duration in courses:
            if total_time + time <= duration:
                # Python 默认是小根堆
                heapq.heappush(time_queue, -time)
                total_time += time
            elif time_queue and time < -time_queue[0]:
                # 这里注意 time_queue中储存的是负值
                total_time += time_queue[0] + time
                heapq.heappop(time_queue)
                heapq.heappush(time_queue, -time)
        return len(time_queue)


class Solution2:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 注意这个排序的key
        # 对于两门课 (t1, d1),(t2, d2),假设有d1 <= d2，则先学习前者，总是最优的
        courses.sort(key=lambda x: x[1])
        total_time = 0
        queue = []

        for time, duration in courses:
            if total_time + time <= duration:
                total_time += time
                # python 默认小根堆
                heapq.heappush(queue, -time)
            elif queue and time < -queue[0]:
                total_time += heapq.heappop(queue) + time
                heapq.heappush(queue, -time)
        return len(queue)


class Solution3:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time_total = 0
        time_queue = []

        for time, duration in courses:
            if time + time_total <= duration:
                time_total += time
                heapq.heappush(time_queue, -time)
            elif time_queue and -time_queue[0] > time:
                time_total += heapq.heappop(time_queue) + time
                heapq.heappush(time_queue, -time)
        return len(time_queue)


if __name__ == '__main__':
    courses = [[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]]
    s = Solution3()
    print(s.scheduleCourse(courses))
