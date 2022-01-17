# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2111_k_increasing
@time: 2021/12/20 11:42 上午
@desc: 
"""
import bisect
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            sub = arr[i::k]
            lis = []
            for num in sub:
                if not lis or num >= lis[-1]:
                    lis.append(num)
                else:
                    loc = bisect.bisect_right(lis, num)
                    lis[loc] = num
            ans += len(sub) - len(lis)
        return ans



class Solution2:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            sub = arr[i::k]
            lis = []
            for num in sub:
                if not lis or num >= lis[-1]:
                    lis.append(num)
                else:
                    loc = bisect.bisect_right(lis, num)
                    lis[loc] = num
            ans += len(sub) - len(lis)
        return ans

