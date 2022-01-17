# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 155_min_stack
@time: 2021/11/30 7:59 下午
@desc: 
"""
import math


class MinStack:

    def __init__(self):
        self.min_num = float("inf")
        self.list = []

    def push(self, val: int) -> None:
        self.list.append(val)
        self.min_num = min(self.min_num, val)

    def pop(self) -> None:
        tmp = self.list.pop()
        if tmp == self.min_num:
            self.min_num = float("inf")
            for i in self.list:
                if self.min_num > i:
                    self.min_num = i

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min_num


class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    s = MinStack2()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())
