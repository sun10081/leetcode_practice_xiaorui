# coding=utf-8

from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == '':
            return -1
        res_dict = {}
        for i in s:
            if res_dict.__contains__(i):
                res_dict[i] += 1
            else:
                res_dict[i] = 1
        for index, char in enumerate(s):
            if res_dict[char] == 1:
                return index
        return -1


if __name__ == '__main__':
    s = 'cc'
    c = Solution()
    res = c.firstUniqChar(s)
    print(res)
