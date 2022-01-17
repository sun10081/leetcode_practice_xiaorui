# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1_count_[oints
@time: 2021/12/12 10:56 上午
@desc: 
"""
from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        # 'R'、'G'、'B'
        count = [[0, 0, 0] for i in range(10)]
        for i in range(1, len(rings), 2):
            index = int(rings[i])
            if rings[i - 1] == "R":
                count[index][0] += 1
            elif rings[i - 1] == "G":
                count[index][1] += 1
            elif rings[i - 1] == "B":
                count[index][2] += 1
        ans = 0
        for array in count:
            if array[0] and array[1] and array[2]:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    rings = "G4"
    print(s.countPoints(rings))




