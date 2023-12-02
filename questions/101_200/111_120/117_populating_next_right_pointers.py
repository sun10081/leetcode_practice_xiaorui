# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 117_populating_next_right_pointers.py
@time: 2023-11-03 09:34:43
"""
from typing import List
from questions.public import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = [root]
        while cur:
            the_next = []
            for i, node in enumerate(cur):
                if i < len(cur) - 1:
                    node.next = cur[i + 1]
                else:
                    node.next = None

                if node.left:
                    the_next.append(node.left)
                if node.right:
                    the_next.append(node.right)
            cur = the_next
        return root
