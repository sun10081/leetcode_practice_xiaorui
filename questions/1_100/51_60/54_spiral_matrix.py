# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 54_spiral_matrix.py
@time: 2022-10-10 01:46:01
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.spiralOrder(matrix))
