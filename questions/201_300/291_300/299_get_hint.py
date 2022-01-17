# coding=utf-8


from typing import List
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        counts_s = [0] * 10
        counts_g = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                counts_s[int(s)] += 1
                counts_g[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(counts_s, counts_g))
        return str(bulls) + "A" + str(cows) + "B"


if __name__ == '__main__':
    secret = "1123"
    guess = "0111"
    s = Solution()
    print(s.getHint(secret, guess))

