# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2022/1/9 10:29 上午
@desc: 
"""
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        ans = [i for i in range(1, n + 1)]
        matrix_a = zip(*matrix)
        matrix_b = [list(arr) for arr in matrix_a]
        for arr in matrix:
            arr.sort()
            if ans != arr:
                return False
        for arr in matrix_b:
            arr.sort()
            if ans != arr:
                return False
        return True


class Solution2:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        nums = set(range(1, len(matrix) + 1))
        return all(set(row) == nums for row in matrix) and all(set(col) == nums for col in zip(*matrix))


if __name__ == '__main__':
    # matrix = [[1,2,1],[1,2,3],[1,2,3]]
    # s = Solution()
    # print(s.checkValid(matrix))
    a = [1, 2, 2, 4, 4, 3, 3]
    b = set(a)
    c = {1, 2, 3, 4}
    print(b == c)
