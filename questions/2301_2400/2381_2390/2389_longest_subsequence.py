# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2389_longest_subsequence.py
@time: 2023-03-17 10:08:57 
"""
from typing import List
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        n, m = len(nums), len(queries)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        ans = []
        for query in queries:
            index = self.binary_search_right(pre_sum, query)
            ans.append(index - 1)
        return ans

    def binary_search_right(self, nums: List[int], x: int):
        l, r = 0, len(nums)
        while l < r:
            mid = l + r >> 1
            if nums[mid] > x:
                r = mid
            else:
                l = mid + 1
        return l

    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        pre_sum = list(accumulate(sorted(nums)))
        ans = [bisect_right(pre_sum, query) for query in queries]
        return ans


if __name__ == '__main__':
    nums = [2, 3, 4, 5]
    queries = [1]
    s = Solution()
    print(s.answerQueries2(nums, queries))
