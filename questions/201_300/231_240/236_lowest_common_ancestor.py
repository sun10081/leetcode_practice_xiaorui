# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 236_lowest_common_ancestor
@time: 2021/12/5 6:28 下午
@desc: 
"""
from questions.public import TreeNode


class Solution:
    def __init__(self):
        self.ans = TreeNode()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            if not root:
                return False
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
                self.ans = root
            return lson or rson or (root.val == p.val or root.val == q.val)

        dfs(root, p, q)
        return self.ans

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor2(root.left, p, q)
        r = self.lowestCommonAncestor2(root.right, p, q)
        if l and r:
            return root
        if not r:
            return l
        return r
