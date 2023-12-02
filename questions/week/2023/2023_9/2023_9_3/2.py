# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/9/3 10:46 AM
@desc:
"""
from typing import List


class Solution:
    def minimumOperations(self, num: str) -> int:
        ans = float('inf')
        n = len(num)
        for i in range(n - 1, -1, -1):
            if num[i] == '0':
                for j in range(i - 1, -1, -1):
                    if num[j] in ['0', '5']:
                        tmp = (n - 1 - i) + (i - j - 1)
                        ans = min(ans, tmp)
            elif num[i] == '5':
                for j in range(i - 1, -1, -1):
                    if num[j] in ['2', '7']:
                        tmp = (n - 1 - i) + (i - j - 1)
                        ans = min(ans, tmp)
        if ans > 100:
            if '0' in num:
                return n - 1
            else:
                return n
        return ans


if __name__ == '__main__':
    s = Solution()
    num = "1"
    print(s.minimumOperations(num))