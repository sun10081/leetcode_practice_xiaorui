# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2934_minimum_operations.py
@time: 2023-11-15 12:20:10 
"""
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # 不交换
        ans_not_swap = 0
        for i in range(n):
            if nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                continue
            elif nums1[i] <= nums2[-1] and nums2[i] <= nums1[-1]:
                ans_not_swap += 1
            else:
                ans_not_swap = -1
                break
        # 交换
        ans_swap = 1
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        for i in range(n):
            if nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                continue
            elif nums1[i] <= nums2[-1] and nums2[i] <= nums1[-1]:
                ans_swap += 1
            else:
                ans_swap = -1
                break
        if ans_swap == -1 and ans_not_swap == -1:
            return -1
        if ans_swap == -1 or ans_not_swap == -1:
            return max(ans_swap, ans_not_swap)
        return min(ans_swap, ans_not_swap)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 7]
    nums2 = [4, 5, 3]
    print(s.minOperations(nums1, nums2))
