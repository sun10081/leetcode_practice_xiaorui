# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 120_minimum_total
@time: 2021/12/22 3:55 下午
@desc: 
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dp 简单模拟 O(n^2)
        :param triangle:
        :return:
        """
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][0]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        """
        自底向上dp O(n)
        :param triangle:
        :return:
        """
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        # todo
        pass


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    print(s.minimumTotal(triangle))

