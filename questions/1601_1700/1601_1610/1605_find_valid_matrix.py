# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1605_find_valid_matrix.py
@time: 2023-03-14 11:23:42 
"""
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            cur_row_sum = rowSum[i]
            for j in range(n):
                tmp = min(cur_row_sum, colSum[j])
                ans[i][j] = tmp
                cur_row_sum -= tmp
                colSum[j] -= tmp

        return ans

    def restoreMatrix2(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            cur_row_sum = rowSum[i]
            for j in range(n):
                tmp = min(cur_row_sum, colSum[j])
                ans[i][j] = tmp
                cur_row_sum -= tmp
                colSum[j] -= tmp
        return ans







if __name__ == '__main__':
    s = Solution()
    rowSum = [14, 9]
    colSum = [6, 9, 8]
    print(s.restoreMatrix(rowSum, colSum))

