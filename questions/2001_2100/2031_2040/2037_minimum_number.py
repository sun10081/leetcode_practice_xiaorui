# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2037_minimum_number.py
@time: 2022-12-31 07:52:41 
"""
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for student, seat in zip(students, seats):
            ans += abs(student - seat)
        return ans


if __name__ == '__main__':
    seats = [3, 1, 5]
    students = [2, 7, 4]
    s = Solution()
    print(s.minMovesToSeat(seats, students))