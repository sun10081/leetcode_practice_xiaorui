# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 543_diameter_of_binary_tree
@time: 2021/12/1 3:39 下午
@desc: 
"""
from questions.public import TreeNode


class Solution:
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 统计的是节点数量
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l + r + 1)
            return max(l, r) + 1

        depth(root)
        return self.ans - 1
