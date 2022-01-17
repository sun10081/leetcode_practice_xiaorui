# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 448_find_disappeared_numbers
@time: 2021/11/30 11:15 下午
@desc: 
"""
from typing import List
from collections import defaultdict


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        """
        哈希
        :param nums:
        :return:
        """
        ans = []
        count = defaultdict(int)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for i in range(1, len(nums) + 1):
            if i not in count:
                ans.append(i)
        return ans

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        """
        原地修改数组
        :param nums:
        :return:
        """
        for num in nums:
            nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        ans = []
        for i, v in enumerate(nums):
            if v > 0:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.findDisappearedNumbers2(nums))
