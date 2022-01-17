from typing import List
from questions.public import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归
        :param root:
        :return:
        """

        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        :param root:
        :return:
        """
        res = []
        if not root:
            return res

        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        recursion
        :param root:
        :return:
        """
        def pre_order(root: TreeNode):
            if not root:
                return
            ans.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        ans = []
        pre_order(root)
        return ans

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        iteration
        :param root:
        :return:
        """
        ans = []
        if not root:
            return ans
        stack = []
        while stack or root:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            # root为None 需要返回上一个有效节点
            root = stack.pop()
            # 向右遍历
            root = root.right
        return ans

