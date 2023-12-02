# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1448_count_good_nodes.py
@time: 2023-08-25 11:41:56 
"""
from typing import List
from questions.public import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            if not node:
                return 0
            res = 0
            if node.val >= path_max:
                res += 1
                path_max = node.val
            res += dfs(node.left, path_max) + dfs(node.right, path_max)
            return res

        return dfs(root, -float('inf'))
