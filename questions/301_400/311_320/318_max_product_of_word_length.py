# coding=utf-8

from typing import List
from collections import defaultdict


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = len(words)
        masks = defaultdict(int)
        # masks = [0] * l
        for i in range(l):
            mask = 0
            for c in words[i]:
                mask |= 1 << (ord(c) - ord("a"))
            masks[mask] = max(masks[mask], len(words[i]))

        max_product = 0
        for i in masks:
            for j in masks:
                if i & j == 0:
                    max_product = max(max_product, masks[i] * masks[j])
        return max_product

class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        l = len(words)
        masks = [0] * l
        for i in range(l):
            for c in words[i]:
                masks[i] |= 1 << (ord(c) - ord("a"))

        max_product = 0
        for i in range(l):
            for j in range(i + 1, l):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product


class Solution3:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        masks = defaultdict(int)
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[mask] = max(masks[mask], len(word))

        for i in masks:
            for j in masks:
                if i & j == 0:
                    ans = max(ans, masks[i] * masks[j])
        return ans


if __name__ == '__main__':
    words = ["meet", "met"]
    s = Solution2()
    print(s.maxProduct(words))
