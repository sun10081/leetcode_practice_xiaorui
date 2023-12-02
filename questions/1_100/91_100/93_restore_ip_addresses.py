# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 93_restore_ip_addresses.py
@time: 2023-11-07 12:26:58 
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(i):
            if i == n and len(path) == 4:
                ans.append('.'.join(path))

            if n - i < 4 - len(path) or n - i > 3 * (4 - len(path)):\
                return

            for j in range(i, i + 4):
                if j < n:
                    sub = s[i: j + 1]
                    if len(sub) > 1 and sub[0] == '0':
                        continue
                    if int(sub) > 255:
                        continue
                    path.append(sub)
                    dfs(j)
                    path.pop()

        ans = []
        path = []
        n = len(s)
        if n < 4 or n > 12:
            return ans
        dfs(0)
        return ans


if __name__ == '__main__':
    s = 'adadsdasads'
    print(s[1:2])