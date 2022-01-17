# coding=utf-8
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n + 0.5))
