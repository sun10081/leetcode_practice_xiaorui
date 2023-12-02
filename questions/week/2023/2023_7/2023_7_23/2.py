# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/7/23 11:10 AM
@desc:
"""
from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        s1 = self.max_value(nums)
        nums.reverse()
        s2 = self.max_value(nums)
        return max(s1, s2)

    def max_value(self, nums: List[int]) -> int:
        s = [nums[0]]
        n = len(nums)
        for i in range(0, n - 1):
            if nums[i] <= nums[i + 1]:
                s.append(s[i] + nums[i + 1])
            else:
                s.append(nums[i + 1])

        return max(s)


if __name__ == '__main__':
    solution = Solution()
    nums = [34, 95, 50, 12, 25, 100, 21, 3, 25, 16, 76, 73, 93, 46, 18]
    print(solution.maxArrayValue(nums))
