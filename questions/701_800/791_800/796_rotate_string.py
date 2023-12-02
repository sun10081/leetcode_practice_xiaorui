# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 796_rotate_string.py
@time: 2022-04-07 09:12:39 
"""
from typing import List


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

    def rotateString2(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s) - 1):
            if s[i + 1:] + s[0:i + 1] == goal:
                return True
        return False


if __name__ == '__main__':
    solu = Solution()
    s = "abcde"
    goal = "cdeab"
    print(solu.rotateString2(s, goal))
