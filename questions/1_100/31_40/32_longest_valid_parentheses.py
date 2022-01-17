# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 32_longest_valid_parentheses
@time: 2021/12/16 2:21 下午
@desc: 
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0
        left, right = 0, 0
        # 从左向右移动
        for i in range(n):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                right += 1

            if left and left == right:
                ans = max(ans, 2 * left)
            elif right > left:
                left = right = 0

        left, right = 0, 0
        # 从右向左移动
        for i in range(n - 1, -1, -1):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                right += 1

            if right and left == right:
                ans = max(ans, 2 * left)
            elif left > right:
                left = right = 0

        return ans


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        left, right = 0, 0
        ans = 0
        # 从左向右
        for i in range(n):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            if left == right:
                ans = max(ans, left * 2)
        # 从右向左
        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left > right:
                left = right = 0
            if left == right:
                ans = max(ans, right * 2)
        return ans


if __name__ == '__main__':
    s = ")()())"
    solution = Solution2()
    print(solution.longestValidParentheses(s))
