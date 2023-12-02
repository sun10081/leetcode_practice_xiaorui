# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 198_house_robber
@time: 2021/12/3 6:52 下午
@desc: 
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * (n + 1)
        dp[-1], dp[0] = 0, nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

    def rob2(self, nums: List[int]) -> int:
        """
        滚动数组
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        first = nums[0]
        second = max(first, nums[1])
        for i in range(2, n):
            first, second = second, max(second, first + nums[i])
        return second


class Solution2:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1], dp[0] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        first, second = 0, nums[0]
        for i in range(1, len(nums)):
            first, second = second, max(second, first + nums[i])
        return second


class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1], dp[0] = 0, nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        first, second = 0, nums[0]
        for i in range(1, n):
            first, second = second, max(first + nums[i], second)
        return second


class Solution4:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        first, second = 0, nums[0]
        for i in range(1, n):
            second, first = max(second, first + nums[i]), second
        return second


if __name__ == '__main__':
    nums = [1, 1]
    # 2, 2, 3, 4
    s = Solution4()
    print(s.rob(nums))
