# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 3
@time: 2023/11/26 10:29 AM
@desc:
"""
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted(zip(nums, range(n)))
        ans = [0] * n
        # 分组循环
        # 外层 准备工作
        i = 0
        while i < n:
            st = i
            i += 1
            # 内层 找最长连续段的末尾
            while i < n and arr[i][0] - arr[i - 1][0] <= limit:
                i += 1
            # 提出arr[st:i]坐标
            idx = sorted(i for _, i in arr[st:i])
            # 赋值
            for j, (x, _) in zip(idx, arr[st:i]):
                ans[j] = x
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [5, 100, 44, 45, 16, 30, 14, 65, 83, 64]
    limit = 15
    print(s.lexicographicallySmallestArray(nums, limit))
