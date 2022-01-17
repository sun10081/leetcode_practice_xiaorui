# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1_find_even_numbers
@time: 2021/12/5 11:11 上午
@desc: 
"""
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n <= 2:
            return []
        ans = []
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for x in range(n):
                    if x == i or x == j:
                        continue
                    if digits[x] % 2 == 0:
                        ans.append(digits[i] * 100 + digits[j] * 10 + digits[x])
        ans = list(set(ans))
        ans.sort()
        return ans


if __name__ == '__main__':
    digits = [2,1,3,0]
    s = Solution()
    print(s.findEvenNumbers(digits))
