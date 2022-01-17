# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 191_count_bits
@time: 2021/12/22 3:39 下午
@desc: 
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n & (1 << i):
                ans += 1
        return ans

    def hammingWeight2(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1
        return ans


if __name__ == '__main__':
    n = 7
    s = Solution()
    print(s.hammingWeight2(n))
