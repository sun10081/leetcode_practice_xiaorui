# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 846_hand_of_straights
@time: 2021/12/30 10:15 上午
@desc: 
"""
from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()
        if n % groupSize:
            return False
        count = Counter(hand)
        for begin_poker in hand:
            if count[begin_poker] == 0:
                continue
            for next_poker in range(begin_poker, begin_poker + groupSize):
                if count[next_poker] == 0:
                    return False
                count[next_poker] -= 1
        return True


if __name__ == '__main__':
    hand = [8, 10, 12]
    group_size = 3
    s = Solution()
    print(s.isNStraightHand(hand, group_size))