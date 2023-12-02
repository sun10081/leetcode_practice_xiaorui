# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/11/25 10:27 PM
@desc:
"""
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        h_max, cur_h = 1, 1
        for i in range(len(hBars) - 1):
            if hBars[i] == hBars[i + 1] - 1:
                cur_h += 1
                h_max = max(h_max, cur_h)
            else:
                cur_h = 1
        v_max, cur_v = 1, 1
        for i in range(len(vBars) - 1):
            if vBars[i] == vBars[i + 1] - 1:
                cur_v += 1
                v_max = max(v_max, cur_v)
            else:
                cur_v = 1
        l = min(h_max, v_max) + 1
        return l * l

    def maximizeSquareHoleArea2(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_ans(nums: List[int]) -> int:
            nums.sort()
            l_max, cur_l = 1, 1
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1] - 1:
                    cur_l += 1
                    l_max = max(l_max, cur_l)
                else:
                    cur_l = 1
            return l_max

        h, v = get_ans(hBars), get_ans(vBars)
        l = min(h, v) + 1
        return l * l


if __name__ == '__main__':
    s = Solution()
    n = 2
    m = 3
    hBars = [2, 3]
    vBars = [2, 3, 4]
    print(s.maximizeSquareHoleArea(n, m, hBars, vBars))

