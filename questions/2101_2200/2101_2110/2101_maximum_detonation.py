# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2101_maximum_detonation
@time: 2021/12/17 11:32 上午
@desc: 
"""
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        data = [[] for _ in range(n)]
        # 收集某炸弹能引爆的所有炸弹，即维护有向图
        for i in range(n):
            for j in range(n):
                if i != j and bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    data[i].append(j)

        ans = 0

        for i in range(n):
            visited = [False] * n
            visited[i] = True
            queue = [i]
            point = 0
            while point < len(queue):
                cur_bomb = queue[point]
                for j in data[cur_bomb]:
                    if not visited[j]:
                        queue.append(j)
                        visited[j] = True
                point += 1
                if len(queue) > ans:
                    ans = len(queue)
        return ans


if __name__ == '__main__':
    s = Solution()
    bombs = [[2, 1, 3], [6, 1, 4]]
    print(s.maximumDetonation(bombs))
