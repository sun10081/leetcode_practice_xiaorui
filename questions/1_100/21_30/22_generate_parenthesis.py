# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 22_generate_parenthesis
@time: 2021/12/5 1:19 上午
@desc: 
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s: List[str], left: int, right: int):
            if len(s) == 2 * n:
                ans.append("".join(s))
                print("生成s {}".format("".join(s)))
                return
            # 左括号最多n个，数量不够时可以添加左括号
            if left < n:
                s.append("(")
                print("添加左括号: {}".format("".join(s)))
                dfs(s, left + 1, right)
                s.pop()
                print("s pop(): {}".format("".join(s)))
            # 数量不够时可以添加右括号
            if left > right:
                s.append(")")
                print("添加右括号: {}".format("".join(s)))
                dfs(s, left, right + 1)
                s.pop()
                print("s pop(): {}".format("".join(s)))

        ans = []
        dfs([], 0, 0)
        return ans


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s: List[str], left_count: int, right_count: int):
            if len(s) == 2 * n:
                ans.append("".join(s))
                return
            if left_count < n:
                s.append("(")
                dfs(s, left_count + 1, right_count)
                s.pop()
            if right_count < left_count:
                s.append(")")
                dfs(s, left_count, right_count + 1)
                s.pop()

        ans = []
        dfs([], 0, 0)
        return ans


class Solution3:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(sequence: List[str], left_count: int, right_count: int):
            if len(sequence) == n * 2:
                ans.append("".join(sequence))
            if left_count < n:
                sequence.append("(")
                dfs(sequence, left_count + 1, right_count)
                sequence.pop()
            if right_count < left_count:
                sequence.append(")")
                dfs(sequence, left_count, right_count + 1)
                sequence.pop()

        ans = []
        dfs([], 0, 0)
        return ans


if __name__ == '__main__':
    n = 8
    s = Solution3()
    print(s.generateParenthesis(n))
