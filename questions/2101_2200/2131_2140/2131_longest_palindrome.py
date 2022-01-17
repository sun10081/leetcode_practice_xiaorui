# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2131_longest_palindrome.py
@time: 2022-01-12 23:56:25 
"""
from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        ans = 0
        has_middle = False
        for word, value in count.items():
            # 本身便是回文串的情况 如gg
            if word == word[::-1]:
                if value % 2:
                    ans += (value - 1) * 2
                    has_middle = True
                else:
                    ans += value * 2
            # 对应回文串存在的情况 如lc/cl
            elif count.get(word[::-1], 0) > 0:
                tmp = min(count[word], count[word[::-1]])
                ans += 4 * tmp
                count[word] -= tmp
                count[word[::-1]] -= tmp
        if has_middle:
            ans += 2
        return ans


if __name__ == '__main__':
    words = ["lc", "cl", "gg", "ob"]
    s = Solution()
    print(s.longestPalindrome(words))



