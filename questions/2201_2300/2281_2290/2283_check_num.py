# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2283_check_num.py
@time: 2023-01-11 09:09:53 
"""
from typing import List
from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        count = defaultdict(int)
        for s in num:
            count[int(s)] += 1
        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    num = "030"
    print(s.digitCount(num))