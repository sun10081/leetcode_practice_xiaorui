# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 647_palindromic_substrings
@time: 2021/12/4 9:21 下午
@desc: 
"""
from typing import List


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        长度为 n 的字符串会生成 2n−1 组回文中心, l = i / 2, r = l + i % 2
        这样我们只要从 0 到 2n−1 遍历 i，就可以得到所有可能的回文中心，这样就把奇数长度和偶数长度两种情况统一起来了。
        i   l   r
        0	0	0
        1	0	1
        2	1	1
        3	1	2
        4	2	2
        5	2	3
        6	3	3
        :param s:
        :return:
        """
        if len(s) == 1:
            return 1
        n = len(s)
        ans = 0

        for i in range(2 * n - 1):
            l = i // 2
            r = l + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1
        return ans


class Solution2:

    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        n = len(s)
        ans = 0
        for i in range(n):
            ans += self.center_expand(s, i, i)
            ans += self.center_expand(s, i, i + 1)
        return ans

    def center_expand(self, s, l, r) -> int:
        ans = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            ans += 1
        return ans


class Solution3:

    def __init__(self):
        self.ans = []

    def countSubstrings(self, s: str) -> List:
        if len(s) == 1:
            return [s]
        n = len(s)
        ans = []
        for i in range(n):
            ans.extend(self.center_expand(s, i, i))
            ans.extend(self.center_expand(s, i, i + 1))
        ans.sort()
        return ans

    def center_expand(self, s, l, r) -> List:
        ans = []
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans.append(s[l:r + 1])
            l -= 1
            r += 1
        return ans


if __name__ == '__main__':
    s = "aaa"
    so = Solution3()
    print(so.countSubstrings(s))
