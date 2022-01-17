# coding=utf-8

from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)
        for index, value in enumerate(nums):
            if target - value in nums_map:
                return [nums_map[target - value], index]
            nums_map[value] = index
        return []


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
