# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 819_most_common_word.py
@time: 2022-04-17 22:58:02 
"""
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para_list = paragraph.split()
        for i in range(len(para_list)):
            para_list[i] = para_list[i].lower()
        count = Counter(para_list)
        for key, value in count.most_common():
            if key not in banned:
                return key


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    s = Solution()
    print(s.mostCommonWord(paragraph, banned))