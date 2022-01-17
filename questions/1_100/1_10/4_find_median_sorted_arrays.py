# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 4_find_median_sorted_arrays
@time: 2021/12/13 8:13 下午
@desc: 
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        # 分割线左边元素数量，即两数组一半的数量（奇数要+1）
        total_left = (m + n + 1) // 2
        # 在nums1的区间[0, m]中查找恰当的分割线，因为开始处理过，nums1相对较短，时间复杂度低
        # 分割线需要满足条件 两侧元素数量相同，且左边小于右边
        # 即 nums1[i - 1] <= nums[j] and nums2[j - 1] <= nums1[i]
        left, right = 0, m
        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                # 大了需要左移 下一轮区间[left, i - 1]
                right = i - 1
            else:
                # 下一轮区间[i, right]
                left = i
        nums1_point = left
        nums2_point = total_left - left
        # 处理四个边界情况
        nums1_left_max = nums1[nums1_point - 1] if nums1_point != 0 else float("-inf")
        nums1_right_min = nums1[nums1_point] if nums1_point != m else float("inf")
        nums2_left_max = nums2[nums2_point - 1] if nums2_point != 0 else float("-inf")
        nums2_right_min = nums2[nums2_point] if nums2_point != n else float("inf")

        if (m + n) % 2:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_left = (m + n + 1) // 2

        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                # [left, i - 1]
                right = i - 1
                # [i, right]
            else:
                left = i

        nums1_point = left
        nums2_point = total_left - nums1_point
        nums1_left_max = nums1[nums1_point - 1] if nums1_point != 0 else float("-inf")
        nums1_right_min = nums1[nums1_point] if nums1_point != m else float("inf")
        nums2_left_max = nums2[nums2_point - 1] if nums2_point != 0 else float("-inf")
        nums2_right_min = nums2[nums2_point] if nums2_point != n else float("inf")

        if (m + n) % 2:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m

        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i

        nums1_point = left
        nums2_point = total_left - left
        nums1_left_max = nums1[nums1_point - 1] if nums1_point != 0 else float("-inf")
        nums1_right_min = nums1[nums1_point] if nums1_point != m else float("inf")
        nums2_left_max = nums2[nums2_point - 1] if nums2_point != 0 else float("-inf")
        nums2_right_min = nums2[nums2_point] if nums2_point != n else float("inf")

        if (m + n) % 2:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2


class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_left = (m + n + 1) // 2

        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i

        nums1_point = left
        nums2_point = total_left - nums1_point
        nums1_left_max = nums1[nums1_point - 1] if nums1_point != 0 else float("-inf")
        nums1_right_min = nums1[nums1_point] if nums1_point != m else float("inf")
        nums2_left_max = nums2[nums2_point - 1] if nums2_point != 0 else float("-inf")
        nums2_right_min = nums2[nums2_point] if nums2_point != n else float("inf")

        if (m + n) % 2:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2


class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m

        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i

        nums1_point = left
        nums2_point = total_left - nums1_point
        nums1_left_max = nums1[nums1_point - 1] if nums1_point != 0 else float("-inf")
        nums1_right_min = nums1[nums1_point] if nums1_point != m else float("inf")
        nums2_left_max = nums2[nums2_point - 1] if nums2_point != 0 else float("-inf")
        nums2_right_min = nums2[nums2_point] if nums2_point != n else float("inf")

        if (m + n) % 2:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    s = Solution4()
    print(s.findMedianSortedArrays(nums1, nums2))
