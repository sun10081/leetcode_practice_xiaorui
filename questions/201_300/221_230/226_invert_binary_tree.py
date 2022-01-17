# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: invert_binary_tree
@time: 2021/12/1 4:05 下午
@desc: 
"""
from questions.public import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
