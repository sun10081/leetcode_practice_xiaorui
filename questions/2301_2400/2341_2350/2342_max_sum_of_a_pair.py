# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2342_max_sum_of_a_pair.py
@time: 2023-11-18 01:20:09 
"""
from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = -1
        for num in nums:
            cur_sum = self.get_digit_sum(num)
            if cur_sum in count:
                ans = max(ans, count[cur_sum] + num)
                count[cur_sum] = max(count[cur_sum], num)
            else:
                count[cur_sum] = num
        return ans

    def get_digit_sum(self, num) -> int:
        ans = 0
        while num:
            ans += num % 10
            num //= 10
        return ans


if __name__ == '__main__':
    nums = [229, 398, 269, 317, 420, 464, 491, 218, 439, 153, 482, 169, 411, 93, 147, 50, 347, 210, 251, 366, 401]
    s = Solution()
    print(s.maximumSum(nums))
