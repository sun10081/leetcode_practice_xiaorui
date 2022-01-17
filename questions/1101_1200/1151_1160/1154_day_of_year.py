# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1151_1160
@time: 2021/12/21 10:47 上午
@desc: 
"""
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        # datetime
        date_array = date.split("-")
        year, month, day = date_array[0], date_array[1], date_array[2]
        date1 = datetime.date(year=int(year), month=int(month), day=int(day))
        date2 = datetime.date(year=int(year), month=1, day=1)
        return (date1 - date2).days + 1

    def dayOfYear2(self, date: str) -> int:
        date_array = date.split("-")
        year, month, day = int(date_array[0]), int(date_array[1]), int(date_array[2])
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (not year % 4 and year % 100) or not year % 400:
            month_days[1] += 1
        ans = 0
        for i in range(month - 1):
            ans += month_days[i]
        return ans + day


if __name__ == '__main__':
    date = "2021-12-21"
    s = Solution()
    print(s.dayOfYear2(date))
