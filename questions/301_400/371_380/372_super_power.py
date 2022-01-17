# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 372_super_power
@time: 2021/12/5 9:21 上午
@desc: 
"""
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """
        快速幂 + 取mod运算

        快速幂 res = res^10 * qpow(a, b[i])
        // 模运算性质一：(a + b) % p = (a % p + b % p) % p
        // 模运算性质二：(a - b) % p = (a % p - b % p + p) % p
        // 模运算性质三：(a * b) % p = (a % p * b % p) % p
        // 模运算性质四：a ^ b % p = ((a % p)^b) % p
         举个例子
        // 12345^678 % 1337 = (12345^670 * 12345^8) % 1337
        //                  = ((12345^670 % 1337) * (12345^8 % 1337)) % 1337  ---> 利用性质 三
        //                  = (((12345^67)^10 % 1337) * (12345^8 % 1337)) % 1337  ---> 乘方性质
        //                  = ((12345^67 % 1337)^10) % 1337 * (12345^8 % 1337)) % 1337  ---> 利用性质 四
        //        ``          = (((12345^67 % 1337)^10) * (12345^8 % 1337)) % 1337  ---> 反向利用性质 三
        :param a:
        :param b:
        :return:
        """
        ans = 1
        for i in range(len(b)):
            ans = (self.qpow(ans, 10) * self.qpow(a, b[i])) % 1337
        return ans

    def qpow(self, x: int, n: int) -> int:
        res = 1
        x %= 1337
        while n > 0:
            if n & 1:
                res = (res * x) % 1337
            x = (x * x) % 1337
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    a = 2
    b = [1, 0]
    print(s.superPow(a, b))