# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 20_valid_parentheses
@time: 2021/12/4 9:44 下午
@desc: 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        字符串长度为奇数 直接false
        bad case
        "(("、"){"
        :param s:
        :return:
        """
        if len(s) % 2:
            return False
        stack = []
        for ch in s:
            if ch in ["(", "[", "{"]:
                stack.append(ch)
            else:
                if not stack:
                    return False
                tmp_ch = stack.pop()
                if (tmp_ch + ch) not in ["()", "[]", "{}"]:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = "([)]"
    so = Solution()
    print(so.isValid(s))
