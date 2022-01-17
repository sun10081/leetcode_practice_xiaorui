# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1220_count_vowels_permutation.py
@time: 2022-01-17 10:15:26 
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % mod, (a + i) % mod, (e + o) % mod, i % mod, (i + o) % mod
        ans = sum([a, e, i, o, u]) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 2
    print(s.countVowelPermutation(n))
