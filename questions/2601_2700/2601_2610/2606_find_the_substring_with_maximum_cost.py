# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2606_find_the_substring_with_maximum_cost.py
@time: 2023-08-08 11:38:46 
"""
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        ans = 0
        pre_sum = 0
        val_dict = dict(zip(chars, vals))
        for ch in s:
            ch_val = val_dict.get(ch, ord(ch) - ord('a') + 1)
            pre_sum = max(pre_sum + ch_val, ch_val)
            ans = max(ans, pre_sum)
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "adaa"
    chars = "d"
    vals = [-1000]
    print(solution.maximumCostSubstring(s, chars, vals))
