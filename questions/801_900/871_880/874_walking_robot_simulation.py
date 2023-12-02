# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 874_walking_robot_simulation.py
@time: 2023-07-19 11:45:34 
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        d = 1
        obs = set((x, y) for x, y in obstacles)
        px, py = 0, 0
        for c in commands:
            if c == -1:
                d += 1
                d %= 4
            elif c == -2:
                d -= 1
                d %= 4
            elif c > 0:
                for i in range(c):
                    if (px + directions[d][0], py + directions[d][1]) in obs:
                        break
                    px, py = px + directions[d][0], py + directions[d][1]
                    ans = max(ans, px * px + py * py)
        return ans


if __name__ == '__main__':
    so = Solution()
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    print(so.robotSim(commands, obstacles))
