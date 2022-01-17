# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 590_n_tree_postorder
@time: 2021/12/1 2:56 下午
@desc: 
"""
from typing import List
from questions.public import Node


class Solution:
    def postorder(self, root: Node) -> List[int]:
        """
        recursion
        :param root:
        :return:
        """
        def post_order(root: Node):
            if not root:
                return ans
            for child in root.children:
                post_order(child)
            ans.append(root.val)

        ans = []
        post_order(root)
        return ans

    def postorder2(self, root: Node) -> List[int]:
        """
        iteration 反转前序遍历的思想
        当前的节点为 u，它的子节点为 v1, v2, v3
        后序遍历 [children of v1], v1, [children of v2], v2, [children of v3], v3, u
        反转 u, v3, [children of v3]', v2, [children of v2]', v1, [children of v1]'
        前序遍历 u, v1, [children of v3]', v2, [children of v2]', v3, [children of v1]'
        只需要解决v1～v3的遍历顺序 即可解决
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
            stack.extend(root.children)
        return ans[::-1]

