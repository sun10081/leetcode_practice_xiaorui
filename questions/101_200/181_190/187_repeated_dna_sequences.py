# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 187_repeated_dna_sequences.py
@time: 2023-11-05 01:35:31 
"""
from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = defaultdict(int)
        ans = []
        n = len(s)
        if n < 10:
            return ans
        cur = list(s[:9])
        l = 0
        for r in range(9, n):
            cur.append(s[r])
            while len(cur) > 10:
                cur.pop(0)
                l += 1
            cnt[''.join(cur)] += 1
        for seq, num in cnt.items():
            if num > 1:
                ans.append(seq)
        return ans


if __name__ == '__main__':
    so = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(so.findRepeatedDnaSequences(s))
