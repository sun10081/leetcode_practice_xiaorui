# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 90_subsets_ii.py
@time: 2023-11-07 11:30:06
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            print(path)
            ans.append(path[:])

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        nums.sort()
        ans = []
        path = []
        n = len(nums)
        dfs(0)
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2]
    print(s.subsetsWithDup(nums))