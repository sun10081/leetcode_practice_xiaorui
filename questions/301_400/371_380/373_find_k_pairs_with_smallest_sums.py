# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 373_find_k_pairs_with_smallest_sums.py
@time: 2022-01-14 10:14:58 
"""
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans, arr = [], []
        # 堆中最多放k个数
        arr_len = min(k, m)
        # 遍历nums1
        for i in range(arr_len):
            arr.append((nums1[i] + nums2[0], i, 0))
        # 每次挑选最小的数对加入ans
        while arr and len(ans) < k:
            _, i, j = heapq.heappop(arr)
            ans.append([nums1[i], nums2[j]])
            # 遍历nums2
            if j + 1 < n:
                heapq.heappush(arr, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        arr = [(nums1[i] + nums2[0], i, 0) for i in range(m)]
        while arr and len(ans) < k:
            _, i, j = heapq.heappop(arr)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(arr, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


if __name__ == '__main__':
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    s = Solution2()
    print(s.kSmallestPairs(nums1, nums2, k))
