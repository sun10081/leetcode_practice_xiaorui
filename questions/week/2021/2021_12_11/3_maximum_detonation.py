# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3_maximum_detonation
@time: 2021/12/12 1:31 上午
@desc: 
"""
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        data = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                    data[i].append(j)

        val = 0
        for i in range(n):
            vis = {i}
            q = [i]
            h = 0
            while h < len(q):
                for j in data[q[h]]:
                    if j not in vis:
                        vis.add(j)
                        q.append(j)
                h += 1
            if len(q) > val:
                val = len(q)
        return val


if __name__ == '__main__':
    s = Solution()
    bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    print(s.maximumDetonation(bombs))
