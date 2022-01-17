# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1716_calculate_money_in_leetcode_bank.py
@time: 2022-01-15 15:29:45
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        money = [i for i in range(1, 8)]
        count = n // 7
        ans = 0
        for i in range(1, count + 1):
            ans += sum(money) + 7 * (i - 1)
        remainder = n % 7
        ans += sum(money[:remainder]) + remainder * count
        return ans

    def totalMoney2(self, n: int) -> int:
        ans = 0
        week_num, day_num = divmod(n, 7)
        # week
        first_week_money = 28
        last_week_money = first_week_money + 7 * (week_num - 1)
        ans += (first_week_money + last_week_money) * week_num // 2
        # day
        first_day_money = 1 + week_num
        last_day_money = first_day_money + day_num - 1
        ans += (first_day_money + last_day_money) * day_num // 2
        return ans


if __name__ == '__main__':
    n = 10
    s = Solution()
    print(s.totalMoney2(n))
