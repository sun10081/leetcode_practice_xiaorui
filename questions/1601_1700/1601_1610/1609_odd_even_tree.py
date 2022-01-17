# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1609_odd_even_tree
@time: 2021/12/25 7:07 上午
@desc: 
"""
from typing import Optional
from questions.public.TreeNode import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
        奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
        :param root:
        :return:
        """
        queue = [root]
        level = 0
        while queue:
            cur_level_node_count = len(queue)
            tmp = 0 if not level % 2 else float("inf")
            for _ in range(cur_level_node_count):
                node = queue.pop(0)
                if not level % 2:
                    if not node.val % 2 or tmp >= node.val:
                        return False
                elif level % 2:
                    if node.val % 2 or tmp <= node.val:
                        return False
                tmp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True


class Solution2:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
        奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
        1 <= node.val <= 10^6
        :param root:
        :return:
        """
        level = 0
        queue = [root]
        while queue:
            n = len(queue)
            tmp = 0 if level % 2 == 0 else float("inf")
            for i in range(n):
                cur_node = queue.pop(0)
                if level % 2 == 0:
                    if cur_node.val % 2 == 0 or tmp >= cur_node.val:
                        return False
                elif level % 2:
                    if cur_node.val % 2 or tmp <= cur_node.val:
                        return False
                tmp = cur_node.val

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            level += 1
        return True


if __name__ == '__main__':
    node6 = TreeNode(val=7)
    node5 = TreeNode(val=3)
    node4 = TreeNode(val=3)
    node2 = TreeNode(val=4, left=node4, right=node5)
    node3 = TreeNode(val=2, left=node6)
    node1 = TreeNode(val=5, left=node2, right=node3)
    s = Solution2()
    print(s.isEvenOddTree(node1))
