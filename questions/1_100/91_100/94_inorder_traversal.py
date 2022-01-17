from typing import List
from questions.public.TreeNode import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归
        :param root:
        :return:
        """

        def inorder(root: TreeNode):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def in_order(root: TreeNode):
            if not root:
                return ans
            in_order(root.left)
            ans.append(root.val)
            in_order(root.right)

        ans = []
        in_order(root)
        return ans

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
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
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        recursion
        :param root:
        :return:
        """
        def in_order(node: TreeNode):
            if not node:
                return
            in_order(node.left)
            res.append(node.val)
            in_order(node.right)

        res = []
        in_order(root)
        return res

    def inorderTraversalIteration(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

