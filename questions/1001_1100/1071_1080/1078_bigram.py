# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1078_bigram
@time: 2021/12/26 6:53 上午
@desc: 
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        text_array = text.split(" ")
        for i in range(2, len(text_array)):
            if text_array[i - 2] == first and text_array[i - 1] == second:
                ans.append(text_array[i])
        return ans


if __name__ == '__main__':
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    s = Solution()
    print(s.findOcurrences(text, first, second))

