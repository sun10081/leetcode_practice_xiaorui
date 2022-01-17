# coding=utf-8

from typing import List


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for item in s:
            if item != ')':
                stack.append(item)
            elif item == ')':
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack:
                    stack.pop()
                stack += tmp
        return "".join(stack)
