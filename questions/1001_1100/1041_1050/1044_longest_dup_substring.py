# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1044_longest_dup_substring
@time: 2021/12/23 10:05 上午
@desc: 
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        # 枚举起点
        for i in range(len(s)):
            # 找更长的子串
            while s[i:i + len(ans) + 1] in s[i + 1:]:
                ans = s[i:i + len(ans) + 1]
                if i + len(ans) >= len(s):
                    return ans
        return ans


class Solution2:
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            while s[i: i + len(ans) + 1] in s[i + 1:]:
                ans = s[i:i + len(ans) + 1]
                if i + len(ans) >= len(s[i + 1:]):
                    return ans
        return ans


if __name__ == '__main__':
    s = "banana"
    # print(s[2:10])
    # print(s[2:])
    solu = Solution()
    print(solu.longestDupSubstring(s))
