# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 101_symmetric_tree
@time: 2021/12/3 2:41 下午
@desc: 
"""
from questions.public import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        recursion
        :param root:
        :return:
        """

        def dfs(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root, root)

    def isSymmetric2(self, root: TreeNode) -> bool:
        def bfs(node1: TreeNode, node2: TreeNode):
            queue = [node1, node2]
            while queue:
                node1 = queue.pop(0)
                node2 = queue.pop(0)
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
            return True

        return bfs(root, root)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        recursion, 分两个指针，分别遍历左右子树，对比
        :param root:
        :return:
        """

        def dfs(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root.left, root.right)

    def isSymmetricIteration(self, root: TreeNode) -> bool:
        def bfs(node1: TreeNode, node2: TreeNode) -> bool:
            queue = [node1, node2]
            while queue:
                node1 = queue.pop(0)
                node2 = queue.pop(0)
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
            return True

        return bfs(root, root)


class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        return dfs(root, root)

    def isSymmetric2(self, root: TreeNode) -> bool:
        def bfs(node1: TreeNode, node2: TreeNode) -> bool:
            queue = [node1, node2]
            while queue:
                node1 = queue.pop()
                node2 = queue.pop()
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
            return True
        return bfs(root, root)


