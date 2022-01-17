# coding=utf-8

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        length = len(A)
        inc, desc = True, True
        for index in range(0, length - 1):
            if A[index] > A[index + 1]:
                inc = False
            if A[index] < A[index + 1]:
                desc = False
        return inc or desc
