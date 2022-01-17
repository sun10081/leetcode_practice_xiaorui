# coding=utf-8

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for item in dictionary:
            i = j = 0
            while i < len(s) and j < len(item):
                if s[i] == item[j]:
                    j += 1
                i += 1
            if j == len(item):
                if len(item) > len(res) or (len(item) == len(res) and item < res):
                    res = item
        return res


if __name__ == '__main__':
    s = "abpcplea"
    dictionary = ["a","b","c"]
    c = Solution()
    a = "123"
    d = int(a)
    print(c.findLongestWord(s, dictionary))
