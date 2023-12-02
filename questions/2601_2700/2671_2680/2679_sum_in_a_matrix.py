# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2679_sum_in_a_matrix.py
@time: 2023-07-04 16:54:57 
"""
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        m, n = len(nums), len(nums[0])
        for array in nums:
            array.sort(reverse=True)

        for i in range(n):
            tmp_num = -1
            for j in range(m):
                if nums[j][i] > tmp_num:
                    tmp_num = nums[j][i]
            ans += tmp_num
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
    print(solution.matrixSum(nums))




