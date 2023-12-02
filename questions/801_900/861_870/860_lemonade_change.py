# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 860_lemonade_change.py
@time: 2023-07-22 12:49:17 
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        five, ten = 1, 0
        for i in range(1, len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                five -= 1
                ten += 1
            elif bills[i] == 20 and ten > 0:
                five -= 1
                ten -= 1
            else:
                five -=3
            if five < 0:
                return False
        return True


if __name__ == '__main__':
    bills = [5, 5, 5, 10, 20]
    s = Solution()
    print(s.lemonadeChange(bills))