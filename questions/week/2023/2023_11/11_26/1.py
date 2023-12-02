# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/11/26 10:29 AM
@desc:
"""
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        new_arr = [[0] * n for _ in range(m)]
        for i in range(m):
            flag = i % 2 == 0
            for j in range(n):
                if flag:
                    new_arr[i][j] = mat[i][j - k]
                else:
                    t = (j + k) % n
                    new_arr[i][j] = mat[i][t]
        return new_arr == mat


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]]
    k = 2
    print(s.areSimilar(mat, k))
