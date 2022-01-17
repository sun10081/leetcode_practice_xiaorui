# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3
@time: 2022/1/8 10:16 下午
@desc: 
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        ans = 0
        for word in words:
            if not self.is_pali(word) and word[::-1] in count:
                ans += len(word) * 2
                count[word[::-1]] -= 1
            else:
                count[word] += 1
        tmp = 0
        flag = False
        for word, value in count.items():
            if value > 0 and self.is_pali(word):
                if value == 1:
                    flag = True
                if value % 2 == 0:
                    tmp += value * 2
                elif value % 2 and value > 2:
                    tmp += (value - 1) * 2
        if (tmp != 0 and tmp % 4 == 0) or (tmp == 0 and flag):
            tmp += 2
        return ans + tmp

    def is_pali(self, s: str) -> bool:
        return s == s[::-1]


class Solution2:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        ans = 0
        for word in words:
            count[word] += 1
        for word, value in count.items():
            if not self.is_pali(word):
                while count[word[::-1]] > 0 and count[word] > 0:
                    ans += len(word) * 2
                    count[word[::-1]] -= 1
                    count[word] -= 1
            else:
                while count[word] >= 2:
                    ans += len(word) * 2
                    count[word] -= 2
        return ans

    def is_pali(self, s: str) -> bool:
        return s == s[::-1]


class Solution3:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        ans = 0
        has_middle = False
        for k in count.keys():
            # 分情况讨论 本身便是回文的字符，如gg
            if k == k[::-1]:
                # 最关键的一步 奇数的情况 要-1，并且标记
                ans += (count[k] // 2) * 4
                if count[k] % 2:
                    has_middle = True
            # 对应回文存在 lc / cl
            else:
                k2 = k[::-1]
                if k2 in count and count[k] > 0:
                    cnt = min(count[k], count[k2])
                    ans += cnt * 4
                    count[k] -= cnt
                    count[k2] -= cnt
        if has_middle:
            ans += 2
        return ans


class Solution4:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        count = Counter(words)
        has_middle = False
        for word, value in count.items():
            if word == word[::-1]:
                if value % 2:
                    ans += (value - 1) * 2
                    has_middle = True
                else:
                    ans += value * 2

            elif word[::-1] in count:
                tmp = min(value, count[word[::-1]])
                ans += tmp * 4
                count[word[::-1]] -= tmp
                count[word] -= tmp
        if has_middle:
            ans += 2
        return ans


class Solution5:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        count = Counter(words)
        has_middle = False
        for word, value in count.items():
            if word == word[::-1]:
                if value % 2:
                    ans += (value - 1) * 2
                    has_middle = True
                else:
                    ans += value * 2
            elif word[::-1] in count:
                tmp = min(count[word[::-1]], count[word])
                ans += tmp * 4
                count[word[::-1]] -= tmp
                count[word] -= tmp
        if has_middle:
            ans += 2
        return ans



if __name__ == '__main__':
    words = ["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]
    s = Solution4()
    print(s.longestPalindrome(words))
