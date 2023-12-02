# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 415_add_strings.py
@time: 2023-07-17 11:36:36 
"""
from typing import List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        i, j = len(num1) - 1, len(num2) - 1
        val = 0

        while i >= 0 or j >= 0 or val > 0:
            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])
            res = a + b + val
            val = res // 10
            ans.append(str(res % 10))
            i -= 1
            j -= 1

        ans.reverse()
        return "".join(ans)


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        i, j = len(num1) - 1, len(num2) - 1
        val = 0

        while i >= 0 or j >= 0 or val:
            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])
            tmp = a + b + val
            ans.append(str(tmp % 10))
            val = tmp // 10
            i -= 1
            j -= 1
        ans.reverse()
        return "".join(ans)


if __name__ == '__main__':
    num1 = "456"
    num2 = "10"
    s = Solution2()
    print(s.addStrings(num1, num2))