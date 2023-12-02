# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2611_mice_and_cheese.py
@time: 2023-06-07 18:49:20 
"""
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = []
        for i in range(len(reward2)):
            diff.append(reward1[i] - reward2[i])
        diff.sort(reverse=True)
        return sum(diff[:k]) + sum(reward2)


if __name__ == '__main__':
    s = Solution()
    reward1 = [1, 1, 3, 4]
    reward2 = [4, 4, 1, 1]
    k = 2
    print(s.miceAndCheese(reward1, reward2, k))

