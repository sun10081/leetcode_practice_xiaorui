# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 347_top_k_frequent_elements.py
@time: 2022-01-15 21:03:08 
"""
from typing import List
from collections import OrderedDict, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = OrderedDict(sorted(Counter(nums).items(), key=lambda x: -x[1]))
        ans = []
        for key, _ in count.items():
            if len(ans) < k:
                ans.append(key)
            else:
                break
        return ans

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))
