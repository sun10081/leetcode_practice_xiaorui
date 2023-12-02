# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2900_longest_subsequence_i.py
@time: 2023-10-22 02:59:26 
"""
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        pre = None
        for i, group in enumerate(groups):
            if pre is None or group != pre:
                ans.append(words[i])
                pre = group
        return ans


if __name__ == '__main__':
    n = 3
    words = ["e", "a", "b"]
    groups = [0, 0, 1]
    s = Solution()
    print(s.getWordsInLongestSubsequence(n, words, groups))