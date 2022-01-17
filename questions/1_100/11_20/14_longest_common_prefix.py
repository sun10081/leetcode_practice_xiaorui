# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 14_longest_common_prefix
@time: 2022/1/13 11:47 下午
@desc: 
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_2 = zip(*strs)
        ans = []
        for row in strs_2:
            for i in range(1, len(row)):
                if row[i] != row[0]:
                    return "".join(ans)
            ans.append(row[0])
        return "".join(ans)


if __name__ == '__main__':
    strs = ["a"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
