# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 239_sliding_window_maximum.py
@time: 2023-11-23 12:43:16 
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, num in enumerate(nums):
            while q and num >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if len(q) > k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


if __name__ == '__main__':
    nums = [1]
    k = 1
    s = Solution()
    print(s.maxSlidingWindow(nums, k))