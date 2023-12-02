# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 167_two_sum_two
@time: 2021/12/16 12:39 上午
@desc: 
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n
        while l < r:
            if numbers[l] + numbers[r] == target:
                break
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    s = Solution2()
    print(s.twoSum(numbers, target))
