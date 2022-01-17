# coding=utf-8

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        counter = ans = 0
        for i, num in enumerate(nums):
            if num:
                counter += 1
            else:
                counter -= 1
            if counter in map:
                ans = max(ans, i - map[counter])
            else:
                map[counter] = i
        return ans
