# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2_executeInstructions
@time: 2021/12/26 4:19 下午
@desc: 
"""
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def find_steps(cur_str: str) -> int:
            x, y = startPos[0], startPos[1]
            step = 0
            for ch in cur_str:
                if ch == "U":
                    x -= 1
                elif ch == "D":
                    x += 1
                elif ch == "L":
                    y -= 1
                elif ch == "R":
                    y += 1

                if x < 0 or x >= n or y < 0 or y >= n:
                    return step
                step += 1
            return step

        ans = []
        for i in range(len(s)):
            ans.append(find_steps(s[i:]))
        return ans


if __name__ == '__main__':
    n = 3
    startPos = [0, 1]
    s = "RRDDLU"
    solu = Solution()
    print(solu.executeInstructions(n, startPos, s))
