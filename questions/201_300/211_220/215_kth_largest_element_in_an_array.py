# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 215_kth_largest_element_in_an_array.py
@time: 2022-01-15 18:57:44 
"""
import heapq
import random
import sortedcontainers
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 维护一个长度为k的小根堆，存放前k大个数，最小的数即为所求
        max_heap = []
        for i in range(len(nums)):
            if len(max_heap) < k:
                heapq.heappush(max_heap, nums[i])
            elif nums[i] > max_heap[0]:
                heapq.heapreplace(max_heap, nums[i])
        return max_heap[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 排序
        sort_arr = sortedcontainers.sortedlist.SortedList(nums)
        return sort_arr[len(nums) - k]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # 快速选择
        def quick_select(l: int, r: int, k: int) -> int:
            if l == r:
                return nums[l]
            i, j = l - 1, r + 1
            random_index = random.randrange(l, r, 1)
            x = nums[random_index]
            while i < j:
                i += 1
                while nums[i] < x:
                    i += 1
                j -= 1
                while nums[j] > x:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            # 计算数量 + 1
            sl = j - l + 1
            if k <= sl:
                return quick_select(l, j, k)
            # 右区间 减去sl的数量才是排名
            return quick_select(j + 1, r, k - sl)

        n = len(nums)
        # 升序数组，所以需要转化下k排名
        return quick_select(0, n - 1, n - k + 1)


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 维护一个长度为k的小根堆，存放前k大个数，最小的数即为所求
        min_heap = []
        n = len(nums)
        for i in range(n):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[i])
            elif nums[i] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[i])
        return min_heap[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def quick_select(l: int, r: int, k: int) -> int:
            if l == r:
                return nums[l]
            i, j = l - 1, r + 1
            x = nums[random.randrange(l, r)]
            while i < j:
                i += 1
                while nums[i] < x:
                    i += 1
                j -= 1
                while nums[j] > x:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            sl = j - l + 1
            if k <= sl:
                return quick_select(l, j, k)
            return quick_select(j + 1, r, k - sl)

        return quick_select(0, len(nums) - 1, len(nums) - k + 1)


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(l, r, k):
            if l >= r:
                return nums[l]
            i, j = l - 1, r + 1
            x = nums[random.randrange(l, r)]
            while i < j:
                i += 1
                while nums[i] < x:
                    i += 1
                j -= 1
                while nums[j] > x:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            sl = j - l + 1
            if k <= sl:
                return quick_select(l, j, k)
            return quick_select(j + 1, r, k - sl)
        n = len(nums)
        return quick_select(0, len(nums) - 1, n - k + 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 1
    s = Solution3()
    print(s.findKthLargest(nums, k))
