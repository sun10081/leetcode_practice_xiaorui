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


if __name__ == '__main__':
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    s = Solution()
    print(s.maxProduct(words))
