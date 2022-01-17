# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 98_is_valid_BST
@time: 2021/12/3 4:29 下午
@desc: 
"""
from questions.public.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        recursion
        有效 二叉搜索树定义如下：
        节点的左子树只包含 小于 当前节点的数。
        节点的右子树只包含 大于 当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。
        :param root:
        :return:
        """
        def bfs(node: TreeNode, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not bfs(node.left, lower, val):
                return False
            if not bfs(node.right, val, upper):
                return False
            return True
        return bfs(root)

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        iteration 中序遍历
        :param root:
        :return:
        """
        stack = []
        pre = float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val >= pre:
                return False
            pre = root.val
            root = root.right
        return True


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, low=float("-inf"), high=float("inf")) -> bool:
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            if not dfs(node.left, low, node.val):
                return False
            if not dfs(node.right, node.val, high):
                return False
            return True
        return dfs(root)

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        bfs
        :param root:
        :return:
        """
        if not root:
            return True
        stack = []
        pre_node_value = float("-inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre_node_value:
                return False
            pre_node_value = root.val
            root = root.right
        return True




