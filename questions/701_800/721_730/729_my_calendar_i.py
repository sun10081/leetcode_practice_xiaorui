# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 729_my_calendar_i.py
@time: 2022-07-05 12:34:39 
"""


class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for l, r in self.booked:
            if l < end and r > start:
                return False
        self.booked.append([start, start])
        return True