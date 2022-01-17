# coding=utf-8

from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = SortedList()
        length = len(nums)
        left = right = ret = 0

        while right < length:
            window.add(nums[right])
            while window[-1] - window[0] > limit:
                window.remove(nums[left])
                left = left + 1
            ret = max(ret, right - left + 1)
            right = right + 1
        return right
