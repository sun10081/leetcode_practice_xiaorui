# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 856_score_of_parentheses.py
@time: 2022-10-09 12:36:40 
"""
from typing import List

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[-1]


if __name__ == '__main__':
    so = Solution()
    s = "(()())"
    print(so.scoreOfParentheses(s))
