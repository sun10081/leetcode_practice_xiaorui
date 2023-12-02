# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2300_successful_pairs.py
@time: 2023-11-10 11:00:02 
"""
import math
import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for spell in spells:
            t = math.ceil(success / spell)
            i = self.binary_search_left(potions, t)
            ans.append(n - i)
        return ans

    def binary_search_left(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + r >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


class Solution2:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        n = len(potions)
        for spell in spells:
            t = math.ceil(success / spell)
            i = bisect.bisect_left(potions, t)
            ans.append(n - i)
        return ans


if __name__ == '__main__':
    s = Solution2()
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(s.successfulPairs(spells, potions, success))
