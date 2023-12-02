# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 48_rotate_image
@time: 2021/12/16 12:25 上午
@desc: 
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(reversed(array)) for array in zip(*matrix)]


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i, array in enumerate(zip(*matrix)):
            matrix[i] = list(reversed(array))


class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 上下翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        # 对角翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]










if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]
    s = Solution1()
    s.rotate(matrix)
    print(matrix)