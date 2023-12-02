# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 53_max_sub_array
@time: 2021/11/30 7:50 下午
@desc: 
"""
from typing import List
from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for num in nums:
            pre = max(pre + num, num)
            ans = max(ans, pre)
        return ans

    def maxSubArray2(self, nums: List[int]) -> int:
        ans = -float('inf')
        pre = 0
        for num in nums:
            pre = max(num, pre + num)
            ans = max(ans, pre)
        return ans

    def maxSubArray3(self, nums: List[int]) -> int:
        ans, pre = -inf, 0
        for num in nums:
            pre = max(num, pre + num)
            ans = max(ans, pre)
        return ans


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution2()
    print(s.maxSubArray(nums))
