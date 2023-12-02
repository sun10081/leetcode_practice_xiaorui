# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2437_number_of_valid_clock_times.py
@time: 2023-05-09 10:48:31 
"""
from typing import List


class Solution:
    def countTime(self, time: str) -> int:
        return self.check(time[:2], 24) * self.check(time[3:], 60)

    def check(self, time: str, threshold: int) -> int:
        count = 0
        for i in range(threshold):
            a = time[0] == '?' or (int(time[0]) == i // 10)
            b = time[1] == '?' or (int(time[1]) == i % 10)
            count += a and b
        return count


if __name__ == '__main__':
    s = Solution()
    time = "?5:00"
    print(s.countTime(time))