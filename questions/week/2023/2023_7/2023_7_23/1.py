# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/7/23 10:58 AM
@desc:
"""
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            tmp = word.split(separator)
            for ch in tmp:
                if ch != '':
                    ans.append(ch)
        return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["one.two.three","four.five","six"]
    separator = "."
    print(solution.splitWordsBySeparator(words, separator))