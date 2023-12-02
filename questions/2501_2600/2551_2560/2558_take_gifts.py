# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2558_take_gifts.py
@time: 2023-10-28 09:50:30
"""
import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        while k:
            heapq.heapreplace(gifts, -1 * int(math.sqrt(-gifts[0])))
            k -= 1
        return -sum(gifts)


if __name__ == '__main__':
    gifts = [25, 64, 9, 4, 100]
    k = 4
    s = Solution()
    print(s.pickGifts(gifts, k))