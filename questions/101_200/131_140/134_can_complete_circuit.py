# coding=utf-8

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        start, sum_value, rest = 0, 0, 0
        for i in range(length):
            sum_value += gas[i] - cost[i]
            rest += gas[i] - cost[i]

            if sum_value < 0:
                start = i + 1
                sum_value = 0
        ans = -1 if rest < 0 else start

        return ans
