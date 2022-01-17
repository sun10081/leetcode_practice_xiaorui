# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1576_modify_string
@time: 2022/1/5 10:14 上午
@desc: 
"""

class Solution:
    def modifyString(self, s: str) -> str:
        ans = list(s)
        n = len(ans)
        for i in range(n):
            if ans[i] == "?":
                for ch in "abc":
                    if (i > 0 and ans[i - 1] == ch) or (i < n - 1 and ans[i + 1] == ch):
                        continue
                    else:
                        ans[i] = ch
                        break
        return "".join(ans)


if __name__ == '__main__':
    so = Solution()
    s = "ubv?w"
    print(so.modifyString(s))
