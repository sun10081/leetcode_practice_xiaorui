# coding=utf-8

from questions.public import TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)
        self.ans += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum


if __name__ == '__main__':
    root = TreeNode(val=1, left=2, right=3)
    s = Solution()
    print(s.findTilt(root))
