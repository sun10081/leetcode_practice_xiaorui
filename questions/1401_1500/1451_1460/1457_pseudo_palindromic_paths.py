# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1457_pseudo_palindromic_paths.py
@time: 2023-11-25 20:00:59 
"""
from typing import Optional
from questions.public.TreeNode import TreeNode


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> int:
            if not node:
                return 0
            mask[node.val] ^= 1
            res = 0
            if not node.left and not node.right:
                res += 1 if sum(mask) <= 1 else 0
            else:
                res = dfs(node.left) + dfs(node.right)
            mask[node.val] ^= 1
            return res

        mask = [0] * 10
        return dfs(root)

    def pseudoPalindromicPaths2(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mask=0):
            if not node:
                return 0
            mask ^= node << node.val
            if not node.left and not node.right:
                return 1 if mask & (mask - 1) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root)