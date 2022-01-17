# coding=utf-8

from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())
