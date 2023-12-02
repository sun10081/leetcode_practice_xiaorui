# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2578_split_with_minimum_sum.py
@time: 2023-10-09 11:23:04 
"""


class Solution:
    def splitNum(self, num: int) -> int:
        array = []
        while num:
            array.append(num % 10)
            num //= 10
        array.sort()
        first, second = 0, 0
        for i in range(len(array)):
            if i % 2 == 0:
                first = first * 10 + array[i]
            else:
                second = second * 10 + array[i]
        return first + second

    def splitNum2(self, num: int) -> int:
        stnum = "".join(sorted(str(num)))
        num1, num2 = int(stnum[::2]), int(stnum[1::2])
        return num1 + num2


if __name__ == '__main__':
    s = Solution()
    num = 4325
    print(s.splitNum(num))
