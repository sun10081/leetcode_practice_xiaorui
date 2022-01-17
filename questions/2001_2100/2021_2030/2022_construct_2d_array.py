# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2022_construct_2d_array
@time: 2022/1/1 10:47 上午
@desc: 
"""
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        original_len = len(original)
        ans = []
        if original_len != m * n:
            return ans
        index = 0
        for _ in range(m):
            ans.append(original[index:index + n])
            index += n
        return ans
