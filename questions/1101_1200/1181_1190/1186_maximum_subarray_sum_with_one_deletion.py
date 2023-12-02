# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1186_maximum_subarray_sum_with_one_deletion.py
@time: 2023-08-08 11:49:43 
"""
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = arr[0]
        dp0, dp1 = arr[0], 0
        for i in range(1, len(arr)):
            num = arr[i]
            dp1 = max(dp0, dp1 + num)
            dp0 = max(dp0 + num, num)
            ans = max(ans, dp0, dp1)
        return ans


if __name__ == '__main__':
    arr = [-1, -1, -1, -1]
    s = Solution()
    print(s.maximumSum(arr))
