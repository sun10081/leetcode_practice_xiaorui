# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 50_my_pow
@time: 2021/12/5 5:08 下午
@desc: 
"""


class Solution:
    def myPowIteration(self, x: float, n: int) -> float:
        """
        iteration
        :param x:
        :param n:
        :return:
        """
        res = 1
        x = 1 / x if n < 0 else x
        n = abs(n)
        while n > 0:
            if n & 1:
                res = res * x
            x = x * x
            n = n >> 1
        return res

    def myPow(self, x: float, n: int) -> float:
        """
        recursion
        :param x:
        :param n:
        :return:
        """
        def qpow(n: int) -> float:
            if n == 0:
                return 1.0
            res = qpow(n // 2)
            return res * res * x if n & 1 else res * res

        x = 1 / x if n < 0 else x
        n = abs(n)
        return qpow(n)


if __name__ == '__main__':
    x = 2.00000
    n = 10
    s = Solution()
    print(s.myPow(x, n))
