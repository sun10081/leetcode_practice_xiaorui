# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 961_distribute_coins_in_binary_tree.py
@time: 2023-07-14 21:01:47 
"""
from typing import List, Optional
from questions.public import TreeNode


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return 0, 0
            coins_left, nodes_left = dfs(node.left)
            coins_right, nodes_right = dfs(node.right)
            coins = coins_left + coins_right + node.val
            nodes = nodes_left + nodes_right + 1

            nonlocal ans
            ans += abs(coins - nodes)
            return coins, nodes
        dfs(root)
        return ans
