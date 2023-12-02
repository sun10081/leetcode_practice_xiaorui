# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2023/9/3 10:30 AM
@desc:
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            if self.check_num(i):
                ans += 1
        return ans

    def check_num(self, num):
        pre_sum = 0
        n = len(str(num))
        if n % 2 == 1:
            return False
        while len(str(num)) > n // 2:
            pre_sum += num % 10
            num = num // 10
        post_sum = 0
        while num:
            post_sum += num % 10
            num = num // 10
        return pre_sum == post_sum


if __name__ == '__main__':
    s = Solution()
    low = 1200
    high = 1230
    print(s.countSymmetricIntegers(low, high))
