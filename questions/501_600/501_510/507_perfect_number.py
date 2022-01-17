# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 507_perfect_number
@time: 2021/12/31 9:53 上午
@desc: 
"""
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        ans = 1
        upper = int(math.sqrt(num)) + 1
        for i in range(2, upper):
            if num % i == 0:
                ans += i + num // i
            if ans > num:
                return False
        return ans == num

    def checkPerfectNumber2(self, num: int) -> bool:
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336


if __name__ == '__main__':
    num = 8128
    s = Solution()
    print(s.checkPerfectNumber(num))



