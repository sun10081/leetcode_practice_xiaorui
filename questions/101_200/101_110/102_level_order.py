from typing import List
from questions.public.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                # 从左到右的顺序 所以要pop 0
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 直接添加即可 extend就变成一个数组了
            res.append(level)
        return res


class Solution2:
    def levelOrderBfs(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node: TreeNode, level: int):
            # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
            if len(res) < level:
                res.append([])
            #  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
            # res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
            res[level - 1].append(node.val)
            # 递归的处理左子树，右子树，同时将层数index+1
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        res = []
        if not root:
            return res
        dfs(root, 1)
        return res
