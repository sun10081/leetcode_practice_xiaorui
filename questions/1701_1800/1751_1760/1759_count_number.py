# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1759_count_number.py
@time: 2022-12-26 09:46:28 
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        mod = 10 ** 9 + 7
        n = len(s)
        j = 0
        for i in range(n):
            while j < i and s[i] == s[j]:
                j += 1
            cnt = j - i
            ans += (cnt + 1) * cnt // 2
        return ans % mod


if __name__ == '__main__':
    so = Solution()
    s = "abbcccaa"
    print(so.countHomogenous(s))



