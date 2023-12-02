# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2490_circular_sentence.py
@time: 2023-06-30 11:55:17
"""
from typing import List


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_array = sentence.split()
        n = len(sentence_array)

        for i in range(1, n):
            if sentence_array[i][0] != sentence_array[i - 1][-1]:
                return False

        return sentence_array[0][0] == sentence_array[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    sentence = "Leetcode eisc cool"
    print(solution.isCircularSentence(sentence))