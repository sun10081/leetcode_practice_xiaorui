# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1198_find_smallest.py
@time: 2023-11-09 23:27:42 
"""
from math import inf
from typing import List
from collections import defaultdict


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cnt = defaultdict(int)
        for i in range(m):
            for j in range(n):
                cnt[mat[i][j]] += 1
        ans = inf
        for key in cnt:
            if cnt[key] == m:
                ans = min(ans, key)
        return ans if ans < inf else -1

    def smallestCommonElement2(self, mat: List[List[int]]) -> int:
        path = mat[0]
        for i in range(1, len(mat)):
            path &= mat[i]
        return min(path) if path else -1


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
    print(s.smallestCommonElement(mat))