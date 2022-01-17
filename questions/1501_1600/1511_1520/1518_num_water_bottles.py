# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1518_num_water_bottles
@time: 2021/12/17 12:53 上午
@desc: 
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty_num = numBottles
        while empty_num >= numExchange:
            ans += empty_num // numExchange
            empty_num = empty_num // numExchange + empty_num % numExchange
        return ans

    def numWaterBottles2(self, numBottles: int, numExchange: int) -> int:
        # 分母-1是兑换了新的酒瓶，分子-1是处理边界情况，如4个酒瓶，兑换需要5个空瓶，不-1的话就会多算
        return numBottles + (numBottles - 1) // (numExchange - 1)


if __name__ == '__main__':
    numBottles = 15
    numExchange = 4
    s = Solution()
    print(s.numWaterBottles2(numBottles, numExchange))
