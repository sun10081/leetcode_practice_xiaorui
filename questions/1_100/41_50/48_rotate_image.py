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
        print(matrix)


if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)