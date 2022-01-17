# coding=utf-8

from questions.public.TreeNode import TreeNode


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        """
        深度优先搜索
        :param root:
        :return:
        """
        if root is None:
            return 0
        left_depth = self.maxDepth1(root.left)
        right_depth = self.maxDepth1(root.right)
        return max(left_depth, right_depth) + 1

    def maxDepth2(self, root: TreeNode) -> int:
        """
        广度优先搜索
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
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = TreeNode(val=3, left=9, right=10)
    print(s.maxDepth2(nums))
