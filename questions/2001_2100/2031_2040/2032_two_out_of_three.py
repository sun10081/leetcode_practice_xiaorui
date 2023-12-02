# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2032_two_out_of_three.py
@time: 2022-12-29 09:05:38 
"""
from typing import List
from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = defaultdict(int)

        for i, nums in enumerate([set(nums1), set(nums2), set(nums3)]):
            for num in nums:
                count[num] |= 1 << i

        ans = []
        for k, v in count.items():
            if v & (v - 1):
                ans.append(k)

        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]
    s = Solution()
    print(s.twoOutOfThree(nums1, nums2, nums3))

