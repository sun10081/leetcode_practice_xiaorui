# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1005_largest_sum_after_k_negations
@time: 2021/12/3 10:05 上午
@desc: 
"""
from typing import List
from collections import Counter


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        排序 待优化
        :param nums:
        :param k:
        :return:
        """
        nums.sort()
        for i in range(len(nums)):
            if k == 0 or nums[i] == 0:
                k = 0
                break
            if nums[i] > 0:
                if i == 0:
                    nums[i] = - nums[i]
                    k = 0
                    break
                if k % 2 == 1:
                    if nums[i] < nums[i - 1]:
                        nums[i] = - nums[i]
                    else:
                        nums[i - 1] = - nums[i - 1]
                    k = 0
                    break
            nums[i] = - nums[i]
            k -= 1

        if k > 0 and k % 2 == 1:
            nums[-1] = - nums[-1]

        return sum(nums)

    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:
        """
        题目限定了数据范围 [-100, 100]
        :param nums:
        :param k:
        :return:
        """
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i] > 0:
                i_valid_count = min(k, freq[i])
                ans += -i * i_valid_count * 2
                freq[i] -= i_valid_count
                freq[-i] += i_valid_count
                k -= i_valid_count
                if k == 0:
                    break

        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break
        return ans


class Solution2:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                valid_num_count = min(freq[i], k)
                ans += -i * 2 * valid_num_count
                freq[i] -= valid_num_count
                freq[-i] += valid_num_count
                k -= valid_num_count
            if not k:
                break

        if k and k & 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break
        return ans


if __name__ == '__main__':
    s = Solution2()
    nums = [2, -3, -1, 5, -4]
    k = 2
    print(s.largestSumAfterKNegations(nums, k))
