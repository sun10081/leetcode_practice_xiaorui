# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 833_find_and_replace_in_string.py
@time: 2023-08-15 23:34:56 
"""
from typing import List
from collections import defaultdict


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        cnt = defaultdict()
        for i, ch in enumerate(s):
            cnt[i] = (1, ch)

        n = len(indices)
        for i in range(n):
            index = indices[i]
            if s[index:].startswith(sources[i]):
                cnt[index] = (len(sources[i]), targets[i])

        p = 0
        while p < len(s):
            length, ch = cnt[p]
            ans.append(ch)
            p += length
        return "".join(ans)


class Solution2:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        cnt = defaultdict()
        n = len(s)
        for i in range(n):
            cnt[i] = (1, s[i])

        for i, index in enumerate(indices):
            if s[index:].startswith(sources[i]):
                cnt[index] = (len(sources[i]), targets[i])

        p = 0
        while p < n:
            length, ch = cnt[p]
            ans.append(ch)
            p += length
        return "".join(ans)


if __name__ == '__main__':
    solution = Solution2()
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print(solution.findReplaceString(s, indices, sources, targets))
