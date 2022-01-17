# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1614_max_depth
@time: 2022/1/7 10:29 上午
@desc: 
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        left = 0
        for ch in s:
            if ch == '(':
                left += 1
                ans = max(ans, left)
            elif ch == ')':
                left -= 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "(1)+((2))+(((3)))"
    print(solu.maxDepth(s))
