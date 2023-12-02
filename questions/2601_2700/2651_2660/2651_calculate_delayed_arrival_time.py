# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2651_calculate_delayed_arrival_time.py
@time: 2023-09-08 16:53:48 
"""
from typing import List


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


if __name__ == '__main__':
    arrivalTime = 15
    delayedTime = 9
    s = Solution()
    print(s.findDelayedArrivalTime(arrivalTime, delayedTime))