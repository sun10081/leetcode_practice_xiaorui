# coding=utf-8

from typing import List


class Solution:
    # def sortArrayByParity(self, A: List[int]) -> List[int]:
    #     return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] % 2 > A[right] % 2:
                A[left], A[right] = A[right], A[left]
            if A[left] % 2:
                left += 1
            if A[right] % 2:
                right -= 1
        return A
