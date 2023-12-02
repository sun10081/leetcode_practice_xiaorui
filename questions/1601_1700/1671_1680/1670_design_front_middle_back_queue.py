# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1670_design_front_middle_back_queue.py
@time: 2023-11-28 20:51:42 
"""
from typing import List
from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()
        self.no_ans = -1

    def balance(self):
        # 使两队列长度最多差1 保持每次操作O(1)
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.right:
            return self.no_ans
        val = self.left.popleft() if self.left else self.right.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.right:
            return self.no_ans
        if len(self.left) == len(self.right):
            return self.left.pop()
        return self.right.popleft()

    def popBack(self) -> int:
        if not self.right:
            return self.no_ans
        val = self.right.pop()
        self.balance()
        return val


class FrontMiddleBackQueue2:

    def __init__(self):
        self.left = deque()
        self.right = deque()
        self.no_ans = -1

    def balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.left) + 1 < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.right.appendleft(val)
        else:
            self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.right:
            return self.no_ans
        ans = self.left.popleft() if self.left else self.right.popleft()
        self.balance()
        return ans

    def popMiddle(self) -> int:
        if not self.right:
            return self.no_ans
        if len(self.left) == len(self.right):
            ans = self.left.pop()
        else:
            ans = self.right.popleft()
        return ans

    def popBack(self) -> int:
        if not self.right:
            return self.no_ans
        ans = self.right.pop()
        self.balance()
        return ans
