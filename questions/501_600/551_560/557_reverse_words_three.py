# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 557_reverse_words_three
@time: 2021/12/17 12:32 上午
@desc: 
"""
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))


class Solution2:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution = Solution2()
    print(solution.reverseWords(s))
