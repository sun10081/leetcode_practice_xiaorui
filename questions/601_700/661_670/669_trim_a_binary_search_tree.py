# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 669_trim_a_binary_search_tree.py
@time: 2022-09-10 23:33:33 
"""
from typing import List, Optional
from questions.public.TreeNode import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root