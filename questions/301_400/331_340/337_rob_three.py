# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 337_rob_three
@time: 2021/12/4 1:42 上午
@desc: 
"""

from typing import List, Tuple
from collections import defaultdict
from questions.public import TreeNode


class Solution:
    """
    只考虑了单一层级的情况
    因为前两道同类型题陷入了思维定式 这是不可取的
    """

    def rob_three(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = self.in_order_traversal(root)
        dp = [sum(level) for level in res]
        return self._rob(dp)

    def _rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        first = nums[0]
        second = max(first, nums[1])
        for i in range(2, n):
            first, second = second, max(second, first + nums[i])
        return second

    def in_order_traversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


class Solution2:
    def rob(self, root: TreeNode) -> int:
        """
        dp
        f(o) 表示选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和；
        g(o) 表示不选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和
        :param root:
        :return:
        """

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val + g.get(node.left, 0) + g.get(node.right, 0)
            g[node] = max(f.get(node.left, 0), g.get(node.left, 0)) + max(f.get(node.right, 0), g.get(node.right, 0))

        f = defaultdict()
        g = defaultdict()
        dfs(root)
        return max(f[root], g[root])

    def rob2(self, root: TreeNode) -> int:
        """
        dp 滚动数组，节省哈希表的开销
        :param root:
        :return:
        """

        def dfs(node: TreeNode) -> Tuple[int, int]:
            if not node:
                return 0, 0
            l = dfs(node.left)
            r = dfs(node.right)
            selected = node.val + l[1] + r[1]
            no_selected = max(l[0], l[1]) + max(r[0], r[1])
            return selected, no_selected

        return max(dfs(root))


class Solution3:
    def rob(self, root: TreeNode) -> int:
        """
        dp
        f(o) 表示选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和；
        g(o) 表示不选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和
        :param root:
        :return:
        """
        # 剪枝 递归 状态方程
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            # 注意左右子树可能为空，不能直接取，要用get
            f[node] = node.val + g.get(node.left, 0) + g.get(node.right, 0)
            g[node] = max(f.get(node.left, 0), g.get(node.left, 0)) + max(f.get(node.right, 0), g.get(node.right, 0))

        f = defaultdict()
        g = defaultdict()
        dfs(root)
        return max(f[root], g[root])

    def rob2(self, root: TreeNode) -> int:
        """
        dp 滚动数组，节省空间
        selected -->f
        no_selected -->g
        l[0]/r[0] 选择了该节点
        l[1]/r[1] 未选择该节点
        :param root:
        :return:
        """

        def dfs(node: TreeNode) -> Tuple[int, int]:
            if not node:
                return 0, 0
            l = dfs(node.left)
            r = dfs(node.right)
            selected = node.val + l[1] + r[1]
            no_selected = max(l[0], l[1]) + max(r[0], r[1])
            return selected, no_selected

        return max(dfs(root))


if __name__ == '__main__':
    res = [[3], [2, 3], [3, 1]]
    dp = [sum(level) for level in res]
    print(dp)
