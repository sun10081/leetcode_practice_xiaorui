# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 179_largest_number.py
@time: 2022-01-15 17:19:16 
"""
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
        ans = "".join(nums_str)
        return '0' if ans[0] == '0' else ans


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    s = Solution()
    print(s.largestNumber(nums))
