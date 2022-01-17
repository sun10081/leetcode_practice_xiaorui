# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 231_power_of_two
@time: 2021/12/21 5:26 下午
@desc: 
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 位运算特性
        return n > 0 and (n & (n - 1) == 0)

    def isPowerOfTwo2(self, n: int) -> bool:
        max_two_pow = 2 ** 30
        return n > 0 and max_two_pow % n == 0


if __name__ == '__main__':
    n = 1
    s = Solution()
    print(s.isPowerOfTwo(n))


