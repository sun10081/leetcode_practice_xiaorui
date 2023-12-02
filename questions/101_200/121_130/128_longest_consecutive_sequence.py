# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 128_longest_consecutive_sequence.py
@time: 2023-08-08 18:34:40 
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        start_num, cur_len = 0, 0
        for num in nums_set:
            if num - 1 not in nums_set:
                start_num = num
                cur_len = 1

            while start_num + 1 in nums_set:
                start_num += 1
                cur_len += 1
            ans = max(ans, cur_len)
        return ans


if __name__ == '__main__':
    nums = [0]
    s = Solution()
    print(s.longestConsecutive(nums))

