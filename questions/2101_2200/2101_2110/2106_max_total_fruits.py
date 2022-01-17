# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2106_max_total_fruits
@time: 2022/1/7 12:34 上午
@desc: 
"""
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        ans = 0
        queue = []
        point = 0
        # 先从左边开始，找到能够到达的最远点，并把从最远的开始到startPos的所有水果加起来，同时入队
