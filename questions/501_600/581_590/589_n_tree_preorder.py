# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 589_n_tree_preorder
@time: 2021/12/1 11:20 上午
@desc: 
"""
from typing import List
from questions.public import Node


class Solution:
    def preorder(self, root: Node) -> List[int]:
        """
        recursion
        :param root:
        :return:
        """
        def pre_order(root: Node):
            if not root:
                return ans
            ans.append(root.val)
            for child in root.children:
                pre_order(child)

        ans = []
        pre_order(root)
        return ans

    def preorder2(self, root: Node) -> List[int]:
        """
        iteration
        :param root:
        :return:
        """
        ans = []
        if not root:
            return ans
        stack = [root]
        while stack:
            root = stack.pop()
            ans.append(root.val)
            stack.extend(root.children[::-1])
        return ans