# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/8/6 10:31 AM
@desc:
"""


class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch == 'i':
                ans.reverse()
            else:
                ans.append(ch)
        return "".join(ans)


if __name__ == '__main__':
    solution = Solution()
    s = "poiinter"
    print(solution.finalString(s))

