# coding=utf-8

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x = x & (x - 1)
                ones = ones + 1
            return ones

        return [countOnes(i) for i in range(num + 1)]

    def countBits2(self, num: int) -> List[int]:
        """
        对于正整数 xx，将其二进制表示右移一位，等价于将其二进制表示的最低位去掉，得到的数是 x/2
        如果bits[x/2]的值一直，则可以得到bits[x]的值
        如果 x 是偶数，则 bits[x] = bits[x/2]
        如果 x 是奇数，则 bits[x] = bits[x/2] + 1
        合并得到 bits[x] = bits[x >> 1] + (x&1)
        """
        bits = [0]
        for i in range(num+1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits
