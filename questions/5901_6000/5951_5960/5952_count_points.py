# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 5952_count_points
@time: 2021/12/12 5:02 下午
@desc: 
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        count = [0] * 10
        for i in range(1, len(rings), 2):
            index = int(rings[i])
            if rings[i - 1] == "R":
                count[index] |= 1
            elif rings[i - 1] == "G":
                count[index] |= 2
            elif rings[i - 1] == "B":
                count[index] |= 4
        ans = 0
        for i in range(len(count)):
            if count[i] == 7:
                ans += 1
        return ans


if __name__ == '__main__':
    rings = "B0B6G0R6R0R6G9"
    s = Solution()
    print(s.countPoints(rings))
