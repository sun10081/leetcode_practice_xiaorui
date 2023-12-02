# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1222_queens.py
@time: 2023-09-14 16:40:27 
"""
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions =[(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
        queens_set = set((x, y) for x, y in queens)
        ans = []
        x, y = king

        for direction in directions:
            nx, ny = direction
            cx, cy = x + nx, y + ny
            while 0 <= cx < 8 and 0 <= cy < 8:
                if (cx, cy) in queens_set:
                    ans.append([cx, cy])
                    break
                else:
                    cx, cy = cx + nx, cy + ny
        return ans


if __name__ == '__main__':
    s = Solution()
    queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
    king = [3, 3]
    print(s.queensAttacktheKing(queens, king))