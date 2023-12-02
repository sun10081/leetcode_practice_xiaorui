# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2899_last_visited_integers.py
@time: 2023-10-22 02:46:59 
"""
from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        nums = []
        ans = []
        k = 0
        for word in words:
            if word != 'prev':
                k = 0
                nums.append(int(word))
            else:
                k += 1
                if k <= len(nums):
                    ans.append(nums[::-1][k - 1])
                else:
                    ans.append(-1)
        return ans


if __name__ == '__main__':
    s = Solution()
    words = ["1", "prev", "2", "prev", "prev"]
    print(s.lastVisitedIntegers(words))
