# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2520_count_the_digits.py
@time: 2023-10-26 09:53:17 
"""
from typing import List


class Solution:
    def countDigits(self, num: int) -> int:
        cur = num
        ans = 0
        while cur:
            tmp = cur % 10
            ans += 1 if num % tmp == 0 else 0
            cur //= 10
        return ans


if __name__ == '__main__':
    num = 121
    s = Solution()
    print(s.countDigits(num))