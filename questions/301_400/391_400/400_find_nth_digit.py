# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 400_find_nth_digit
@time: 2021/11/30 10:05 上午
@desc: 
"""

class Solution:
    def findNthDigit1(self, n: int) -> int:
        """
        双指针
        :param n:
        :return:
        """
        pass

    def findNthDigit2(self, n: int) -> int:
        d = 1  # 位数
        count = 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10

        index = n - 1   # 单个数字的index
        start = 10 ** (d - 1)   # 这一组最开始的数字 10的d-1次方
        num = start + index // d    # 目标数字所在的整数
        digit_index = index % d     # 数字在整数中的坐标，从左到右
        digit_index_from_right = d - 1 - digit_index    # 数字在整数中的坐标，从右到左
        return num // 10 ** digit_index_from_right % 10


