from questions.public import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        迭代
        :param root:
        :param val:
        :return:
        """
        if root is None:
            return None
        tree_node = root
        while tree_node and tree_node.val != val:
            tree_node = tree_node.left if tree_node.val > val else tree_node.right
        return tree_node

    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        """
        递归
        :param root:
        :param val:
        :return:
        """
        if root is None:
            return None
        if root.val == val:
            return root
        tree_node = root
        if tree_node.val > val:
            return self.searchBST2(tree_node.left, val)
        return self.searchBST2(tree_node.right, val)
