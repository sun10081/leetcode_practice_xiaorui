# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/11/5 10:24 AM
@desc:
"""
import copy
from typing import List
from collections import defaultdict


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        count = defaultdict(list)
        m = len(edges)
        for i in range(len(edges)):
            u, v = edges[i]
            count[u].append(v)
        ans = -1
        for key, arr in count.items():
            seq = copy.deepcopy(arr)
            i = 0
            while i < len(seq):
                if len(count[seq[i]]) > 0:
                    seq.extend(seq[i])
                i += 1
            if len(seq) == m - 1:
                return key
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 4

    edges = [[0, 2], [1, 3], [1, 2]]
    print(s.findChampion(n, edges))

