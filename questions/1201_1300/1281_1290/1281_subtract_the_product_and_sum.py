# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1281_subtract_the_product_and_sum.py
@time: 2023-08-09 09:46:40 
"""
from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, num_sum = 1, 0
        while n:
            cur = n % 10
            product *= cur
            num_sum += cur
            n //= 10
        return product - num_sum


if __name__ == '__main__':
    n = 4421
    s = Solution()
    print(s.subtractProductAndSum(n))