# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1615_maximal_network_rank.py
@time: 2023-03-15 10:24:28 
"""
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connect = [[False] * n for _ in range(n)]  # 统计连接情况
        degree = [0] * n
        for a, b in roads:
            connect[a][b] = True
            connect[b][a] = True
            degree[a] += 1
            degree[b] += 1

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if connect[i][j]:
                    tmp = degree[i] + degree[j] - 1
                else:
                    tmp = degree[i] + degree[j]
                ans = max(tmp, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 2
    roads = [[1, 0]]
    print(s.maximalNetworkRank(n, roads))

