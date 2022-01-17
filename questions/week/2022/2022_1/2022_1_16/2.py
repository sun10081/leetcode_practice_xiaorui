# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2022/1/16 10:41 上午
@desc: 
"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        ans = 0
        double = maxDoubles
        while target != 1:
            if double > 0:
                if target % 2 == 0:
                    double -= 1
                    ans += 1
                    target = target // 2
                else:
                    target -= 1
                    ans += 1
            else:
                ans += target - 1
                break
        return ans


if __name__ == '__main__':
    target = 656101987
    maxDoubles = 1
    s = Solution()
    print(s.minMoves(target, maxDoubles))