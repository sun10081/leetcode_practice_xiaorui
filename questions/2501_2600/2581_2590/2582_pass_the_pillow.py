# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2582_pass_the_pillow.py
@time: 2023-09-26 23:47:32 
"""
from typing import List


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        the_round, num = divmod(time, n - 1)
        if the_round % 2 == 1:
            return n - num
        return num


if __name__ == '__main__':
    s = Solution()
    n = 9
    time = 4
    print(s.passThePillow(n, time))
