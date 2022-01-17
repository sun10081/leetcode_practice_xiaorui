# coding=utf-8

from questions.public import Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        深度搜索
        :param root:
        :return:
        """
        if root is None:
            return 0
        ans = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            ans = max(ans, child_depth)
        return ans + 1

    def maxDepth2(self, root: Node) -> int:
        """
        广度优先
        :param root:
        :return:
        """
        if root is None:
            return 0
        queue = [root]
        ans = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                for child in node.children:
                    if child:
                        queue.append(child)
            ans += 1
        return ans




