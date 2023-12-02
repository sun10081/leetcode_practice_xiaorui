# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/7/30 11:15 AM
@desc:
"""
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for hour in hours:
            if hour >= target:
                ans += 1
        return ans
