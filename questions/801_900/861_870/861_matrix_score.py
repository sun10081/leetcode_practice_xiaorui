# coding=utf-8

from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        line = len(A)
        row = len(A[0])
        res = line * (1 << (row - 1))

        for j in range(1, row):
            row_counts = 0
            for i in range(0, line):
                if A[i][0]:
                    row_counts += A[i][j]
                else:
                    row_counts += 1 - A[i][j]
            res_line_counts = max(row_counts, line - row_counts)
            res += res_line_counts * (1 << (row - 1 - j))
        return res
