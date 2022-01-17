# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 748_shortest_completing_word
@time: 2021/12/10 10:33 上午
@desc: 
"""
from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = [0] * 26
        for ch in licensePlate:
            # isalpha是否只包含字母, isdigit只包含数字，isalnum包含字母、数字
            if ch.isalpha():
                ch = ch.lower()
                # ord 字符转ascii
                count[ord(ch) - 97] += 1
        min_len = float("inf")
        ans = []
        for word in words:
            word_count = Counter(word)
            for i in range(26):
                # chr ascii转字符
                if count[i] != 0 and count[i] > word_count[chr(97 + i)]:
                    break
            else:
                if len(word) < min_len:
                    min_len = len(word)
                    ans.clear()
                    ans.append(word)
        return ans[0]

    def shortestCompletingWord2(self, licensePlate: str, words: List[str]) -> str:
        # 灵活使用counter， counter之间可以互相加减
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)


if __name__ == '__main__':
    s = Solution()
    licensePlate = "OgEu755"
    words = ["enough", "these", "play", "wide", "wonder", "box", "arrive", "money", "tax", "thus"]
    print(s.shortestCompletingWord2(licensePlate, words))
