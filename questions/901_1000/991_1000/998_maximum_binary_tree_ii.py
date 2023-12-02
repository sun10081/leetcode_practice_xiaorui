# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 998_maximum_binary_tree_ii.py
@time: 2022-08-30 12:38:38 
"""
from typing import Optional
from questions.public.TreeNode import TreeNode

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val > root.val or not root:
            ans = TreeNode(val)
            ans.left = root
            return ans

        root.right = self.insertIntoMaxTree(root.right, val)
        return root