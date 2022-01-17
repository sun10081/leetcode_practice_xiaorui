# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1446_consecutive_characters
@time: 2021/12/1 10:26 上午
@desc: 
"""

class Solution:
    def maxPower(self, s: str) -> int:
        pre, ans = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                pre += 1
                ans = max(ans, pre)
            else:
                pre = 1
        return ans


if __name__ == '__main__':
    s = "hooraaaaaaaaaaay"
    so = Solution()
    print(so.maxPower(s))