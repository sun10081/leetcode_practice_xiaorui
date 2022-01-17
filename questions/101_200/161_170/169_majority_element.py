# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 169_majority_element
@time: 2021/11/30 8:32 下午
@desc: 
"""
import random
from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        """
        随机数
        :param nums:
        :return:
        """
        majority_count = len(nums) // 2
        while True:
            rand_num = random.choice(nums)
            if sum(1 for elem in nums if elem == rand_num) > majority_count:
                return rand_num

    def majorityElement2(self, nums: List[int]) -> int:
        """
        投票算法
        :param nums:
        :return:
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    nums = [1, 2, 1, 1, 1, 2, 2, 2, 2, 2]
    s = Solution()
    print(s.majorityElement2(nums))
