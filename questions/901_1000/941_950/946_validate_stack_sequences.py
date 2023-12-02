# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 946_validate_stack_sequences.py
@time: 2022-08-31 12:51:57 
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, index = [], 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return len(stack) == 0