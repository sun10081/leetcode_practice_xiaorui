# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2511_maximum_enemy_forts.py
@time: 2023-09-02 12:34:25 
"""
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans, pre = 0, -1
        for i, fort in enumerate(forts):
            if fort in (-1, 1):
                if pre > 0 and fort != forts[pre]:
                    ans = max(ans, i - pre - 1)
                pre = i
        return ans


if __name__ == '__main__':
    s = Solution()
    forts = [-1, -1, 0, 1, 0, 0, 1, -1, 1, 0]
    print(s.captureForts(forts))
