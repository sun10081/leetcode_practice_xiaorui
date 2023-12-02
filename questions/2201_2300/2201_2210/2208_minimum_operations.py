# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2208_minimum_operations.py
@time: 2023-07-25 16:05:54 
"""
from typing import List
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            heapq.heappush(ans, -num)
        ori_sum = sum(nums)
        cur_sum = ori_sum
        count = 0
        while cur_sum > ori_sum / 2:
            num = -heapq.heappop(ans) / 2
            cur_sum -= num
            heapq.heappush(ans, -num)
            count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    nums = [3,8,20]
    print(solution.halveArray(nums))





