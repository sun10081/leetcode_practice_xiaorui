# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1116_zero_even_odd
@time: 2021/12/7 5:46 下午
@desc: 
"""
import threading
from threading import Lock
from typing import Callable


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_zero = Lock()
        self.lock_odd = Lock()
        self.lock_even = Lock()
        self.lock_odd.acquire()
        self.lock_even.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        odd_flag = True
        for i in range(self.n):
            self.lock_zero.acquire()
            printNumber(0)
            self.lock_odd.release() if odd_flag else self.lock_even.release()
            odd_flag = not odd_flag

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        evenNum = 2
        end = self.n if self.n % 2 == 0 else self.n - 1
        while evenNum != end + 2:
            self.lock_even.acquire()
            printNumber(evenNum)
            evenNum = evenNum + 2
            self.lock_zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        oddNum = 1
        end = self.n if self.n % 2 != 0 else self.n - 1
        while oddNum != end + 2:
            self.lock_odd.acquire()
            printNumber(oddNum)
            oddNum = oddNum + 2
            self.lock_zero.release()


if __name__ == '__main__':
    n = 2
    s = ZeroEvenOdd(n)




