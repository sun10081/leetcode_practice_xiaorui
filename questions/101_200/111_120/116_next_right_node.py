# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 116_next_right_node
@time: 2021/12/21 12:04 上午
@desc: 
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]

        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                if i != l - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
