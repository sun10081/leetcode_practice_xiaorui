# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2600_k_items.py
@time: 2023-07-05 08:47:57 
"""
from typing import List


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k < numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)


if __name__ == '__main__':
    solution = Solution()
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 2
    print(solution.kItemsWithMaximumSum(numOnes, numNegOnes, numZeros, k))

