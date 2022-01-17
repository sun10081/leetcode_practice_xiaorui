from typing import List
from questions.public import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归
        :param root:
        :return:
        """

        def post_order(root: TreeNode):
            if not root:
                return
            post_order(root.left)
            post_order(root.right)
            res.append(root.val)

        res = []
        post_order(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        :param root:
        :return:
        """
        res = []
        if not root:
            return res

        pre = None
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == pre:
                res.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        recursion
        :param root:
        :return:
        """

        def post_order(root: TreeNode):
            if not root:
                return ans
            post_order(root.left)
            post_order(root.right)
            ans.append(root.val)

        ans = []
        post_order(root)
        return ans

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        iteration
        :param root:
        :return:
        """
        ans = []
        if not root:
            return ans

        stack = []
        pre = None
        # 注意循环条件
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            # root为None 从栈顶取值
            root = stack.pop()
            # 已经遍历到底了，或是右子节点已经被添加过了
            if not root.right or root.right == pre:
                ans.append(root.val)
                pre = root
                root = None
            # 存在未添加过的右子节点 则继续向右遍历
            else:
                stack.append(root)
                root = root.right
        return ans


