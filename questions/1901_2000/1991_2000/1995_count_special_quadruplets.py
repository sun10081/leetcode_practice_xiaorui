# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1995_count_special_quadruplets
@time: 2021/12/29 10:03 上午
@desc: 
"""
from typing import List
from collections import defaultdict


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)
        ans = 0
        for b in range(n - 3, 0, -1):
            # d - c
            for d in range(n - 1, b + 1, -1):
                count[nums[d] - nums[b + 1]] += 1
            for a in range(0, b):
                if (nums[a] + nums[b]) in count:
                    ans += count[nums[a] + nums[b]]
        return ans


class Solution2:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = defaultdict(int)
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                count[nums[d] - nums[b + 1]] += 1
            for a in range(0, b):
                # 重点关注下 [a, b] 匹配所有的[c, d]
                if (nums[a] + nums[b]) in count:
                    ans += count[nums[a] + nums[b]]
        return ans


class Solution3:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = defaultdict(int)
        for b in range(n - 3, 0, -1):
            for d in range(n - 1, b + 1, -1):
                # d - c
                count[nums[d] - nums[b + 1]] += 1
            for a in range(b):
                if count[nums[a] + nums[b]] > 0:
                    ans += count[nums[a] + nums[b]]
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 5]
    s = Solution3()
    print(s.countQuadruplets(nums))
