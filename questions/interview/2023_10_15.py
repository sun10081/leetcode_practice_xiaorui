# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2023_10_15
@time: 2023/10/15 2:41 PM
@desc:
"""
from typing import List


class Solution:
    def reverse_num(self, num: int) -> int:
        flag = 1 if num >= 0 else -1
        num = abs(num)
        ans = 0
        while num:
            ans = ans * 10 + num % 10
            num = num // 10
        return ans * flag


if __name__ == '__main__':
    s = Solution()
    num = -123
    print(s.reverse_num(num))
