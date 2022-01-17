# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 4
@time: 2022/1/9 10:29 上午
@desc: 
"""
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time = list(zip(plantTime, growTime))
        time.sort(key=lambda x: x[1], reverse=True)
        ans, day = 0, 0
        for flower in time:
            day += flower[0]
            ans = max(ans, day + flower[1])
        return ans
