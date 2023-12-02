# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1253_reconstruct_a_2_row_binary_matrix.py
@time: 2023-06-29 17:39:15 
"""
from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        res = [[0] * n for _ in range(2)]
        cnt = 0
        for i in range(n):
            c = colsum[i]
            if c == 0:
                res[0][i] = 0
                res[1][i] = 0
            elif c == 2:
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1
                lower -= 1
            else:
                cnt += 1

        if lower < 0 or upper < 0 or cnt != upper + lower:
            return []
        for i in range(n):
            if colsum[i] == 1:
                if upper:
                    res[0][i] = 1
                    res[1][i] = 0
                    upper -= 1
                else:
                    res[0][i] = 0
                    res[1][i] = 1

        return res


if __name__ == '__main__':
    solution = Solution()
    upper = 2
    lower = 1
    colsum = [1, 1, 1]
    print(solution.reconstructMatrix(upper, lower, colsum))

