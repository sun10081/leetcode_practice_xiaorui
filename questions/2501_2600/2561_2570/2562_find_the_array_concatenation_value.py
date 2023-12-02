# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2562_find_the_array_concatenation_value.py
@time: 2023-10-12 01:42:49 
"""
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            ans += self.concval(nums[i], nums[j])
            i += 1
            j -= 1
        return ans if i > j else ans + nums[i]

    def concval(self, num1: int, num2: int) -> int:
        temp = num2
        while temp:
            num1 *= 10
            temp //= 10
        return num1 + num2




if __name__ == '__main__':
    nums = [5, 14, 13, 8, 12]
    s = Solution()
    print(s.findTheArrayConcVal(nums))
