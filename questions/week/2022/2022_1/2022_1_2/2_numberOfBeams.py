# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2_numberOfBeams
@time: 2022/1/2 10:34 上午
@desc: 
"""
from typing import List
from collections import Counter


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])
        last_count = Counter(bank[0])['1']
        ans = 0
        for i in range(1, m):
            count = Counter(bank[i])['1']
            if count == 0:
                continue
            ans += last_count * count
            last_count = count
        return ans


if __name__ == '__main__':
    s = Solution()
    bank = ["011001","000000","010100","001000"]
    print(s.numberOfBeams(bank))
