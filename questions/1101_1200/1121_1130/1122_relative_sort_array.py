# coding=utf-8

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp_array = [0] * (max(arr1) + 1)
        for x in arr1:
            temp_array[x] += 1
        res_array = []
        for x in arr2:
            res_array.extend([x] * temp_array[x])
            temp_array[x] = 0
        for x in range(max(arr1) + 1):
            if temp_array[x] > 0:
                res_array.extend([x] * temp_array[x])
        return res_array

