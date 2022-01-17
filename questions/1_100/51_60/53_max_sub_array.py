# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 53_max_sub_array
@time: 2021/11/30 7:50 下午
@desc: 
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for num in nums:
            pre = max(pre + num, num)
            ans = max(ans, pre)
        return ans


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))