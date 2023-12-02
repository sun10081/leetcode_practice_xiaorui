# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 944_delete_columns_to_make_sorted.py
@time: 2022-05-12 10:39:34 
"""
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            for i in range(1, len(col)):
                if col[i] < col[i - 1]:
                    ans += 1
                    break
        return ans


if __name__ == '__main__':
    strs = ["zyx", "wvu", "tsr"]
    s = Solution()
    print(s.minDeletionSize(strs))


