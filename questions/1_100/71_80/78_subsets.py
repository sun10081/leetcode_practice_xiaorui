# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 78_subsets
@time: 2021/12/11 12:28 上午
@desc: 
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            print(f"当前i={i}, 将seq={seq}添加ans")
            ans.append(seq[:])

            for j in range(i, n):
                print(f'seq添加nums[j]={nums[j]}')
                seq.append(nums[j])
                dfs(j + 1)
                seq.pop()

        ans = []
        seq = []
        n = len(nums)
        dfs(0)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets(nums))
