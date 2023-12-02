# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2022/11/13 10:29 AM
@desc:
"""
from typing import List
import decimal


class Solution:
    def convertTemperature(self, celsius: float):
        a = round(celsius + 273.15, 5)
        b = round(celsius * 1.8 + 32, 5)
        return [a, b]

    def convert(self, num):
        s = str(num)
        if '.' not in s:
            return float(s + ".00000")
        while len(s) - s.rfind('.') <= 5:
            s += "0"
        return decimal.Decimal(s)


if __name__ == '__main__':
    s = Solution()
    print(s.convertTemperature(36.50))
