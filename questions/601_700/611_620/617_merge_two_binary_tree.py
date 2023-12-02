# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 617_merge_two_binary_tree
@time: 2021/12/1 3:18 下午
@desc: 
"""
from questions.public import TreeNode
from typing import Optional


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        recursion
        :param root1:
        :param root2:
        :return:
        """
        if not root1:
            return root2
        if not root2:
            return root1
        merged_root = TreeNode(root1.val + root2.val)
        merged_root.left = self.mergeTrees(root1.left, root2.left)
        merged_root.right = self.mergeTrees(root2.right, root2.right)
        return merged_root

    def mergeTrees2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        iteration todo
        :param root1:
        :param root2:
        :return:
        """
        pass


class Solution2:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged


class Solution3:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(val=t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged




