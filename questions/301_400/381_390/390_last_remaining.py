# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 390_last_remaining
@time: 2022/1/2 10:04 上午
@desc: 
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        # 等差数列，数组元素个数
        num_amount = n
        # 循环次数，标记删除的方向
        loop_count = 0
        # a0首个元素，d等差数列的间隔
        a, d = 1, 1
        while num_amount != 1:
            # 奇数的情况，首尾元素都会被删除
            if num_amount % 2:
                a += d
            # 偶数的情况，首位删除，末位保留，需要判断删除方向
            else:
                # 从左向右删除时，首位不保留
                if loop_count % 2 == 0:
                    a = a + d
            loop_count += 1
            d *= 2
            num_amount //= 2
        return a


if __name__ == '__main__':
    s = Solution()
    n = 9
    print(s.lastRemaining(n))
