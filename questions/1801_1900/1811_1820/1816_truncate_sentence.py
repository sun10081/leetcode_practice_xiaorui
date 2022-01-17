# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1816_truncate_sentence
@time: 2021/12/6 1:10 上午
@desc: 
"""
import re


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space_num = 0
        for i in range(len(s)):
            if s[i] == " ":
                space_num += 1
            if space_num == k:
                return s[:i]
        return s

    def truncateSentence2(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ')[:k])

    def truncateSentence3(self, s: str, k: int) -> str:
        l = re.findall(r"\w+\b", s)
        return ' '.join(l[:k])


if __name__ == '__main__':
    s = "chopper is not a tanuki"
    k = 4
    so = Solution()
    print(so.truncateSentence3(s, k))
