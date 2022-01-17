# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 689_max_sum_of_three_subarrays
@time: 2021/12/8 10:38 上午
@desc: 
"""
from typing import List


class Solution:
    def maxSumOfOneSubarrays(self, nums: List[int], k: int) -> List[int]:
        sum1, max_sum1 = 0, 0
        ans = []
        for i, num in enumerate(nums):
            if i >= k - 1:
                sum1 += nums[i]
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    ans = [i - k + 1]
                sum1 -= nums[i - k + 1]
        return ans

    def maxSumOfTwoSubarrays(self, nums: List[int], k: int) -> List[int]:
        sum1, max_sum1, max_sum1_index = 0, 0, 0
        sum2, max_sum2 = 0, 0
        ans = []
        for i, num in enumerate(nums):
            if i >= 2 * k - 1:
                sum1 += nums[i - k]
                sum2 += nums[i]
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_sum1_index = i - 2 * k + 1
                if max_sum1 + sum2 > max_sum2:
                    max_sum2 = max_sum1 + sum2
                    ans = [max_sum1_index, i - k + 1]
                sum1 -= nums[i - 2 * k + 1]
                sum2 -= nums[i - k + 1]
        return ans

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sum1, max_sum1, max_sum1_index = 0, 0, 0
        sum2, max_sum2, max_sum2_index, tmp_max_sum1_index = 0, 0, 0, 0
        sum3, max_sum3 = 0, 0
        ans = []
        for i, num in enumerate(nums):
            if i >= 3 * k - 1:
                sum1 += nums[i - 2 * k]
                sum2 += nums[i - k]
                sum3 += nums[i]
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_sum1_index = i - 3 * k + 1
                if max_sum1 + sum2 > max_sum2:
                    tmp_max_sum1_index = max_sum1_index
                    max_sum2 = max_sum1 + sum2
                    max_sum2_index = i - 2 * k + 1
                if max_sum2 + sum3 > max_sum3:
                    max_sum3 = max_sum2 + sum3
                    ans = [tmp_max_sum1_index, max_sum2_index, i - k + 1]
                sum1 -= nums[i - 3 * k + 1]
                sum2 -= nums[i - 2 * k + 1]
                sum3 -= nums[i - k + 1]
        return ans

    def maxSumOfThreeSubarrays2(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        sum2, maxSum12, maxSum12Idx = 0, 0, ()
        sum3, maxTotal = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i - k * 3 + 1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 10, 6, 11, 17, 4, 11, 1, 3]
    k = 1
    print(s.maxSumOfThreeSubarrays(nums, k))
