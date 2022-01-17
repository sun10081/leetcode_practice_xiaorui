# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2099_max_sub_sequence
@time: 2021/12/14 4:42 下午
@desc: 
"""
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = (i, nums[i])
        # 默认升序，这里要改成降序
        nums.sort(key=lambda x: x[1], reverse=True)
        nums = nums[:k]
        nums.sort(key=lambda x: x[0])
        return [sequence[1] for sequence in nums]


class Solution2:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = (i, nums[i])
        nums.sort(key=lambda x: x[1], reverse=True)
        nums = nums[:k]
        nums.sort(key=lambda x: x[0])
        return [array[1] for array in nums]


if __name__ == '__main__':
    nums = [2, 1, 3, 3]
    k = 2
    s = Solution2()
    print(s.maxSubsequence(nums, k))

