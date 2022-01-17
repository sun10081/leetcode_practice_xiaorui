# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1185_day_of_the_week
@time: 2022/1/3 11:12 上午
@desc: 
"""
import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days = 0
        # 年
        days += (year - 1971) * 365 + (year - 1969) // 4
        # 月
        days += sum(month_days[:month - 1])
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month >= 3:
            days += 1
        # 日
        days += day

        # 1970.12.31是星期四
        return week[(days + 3) % 7]

    def dayOfTheWeek2(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")


if __name__ == '__main__':
    year = 2022
    month = 1
    day = 3
    s = Solution()
    print(s.dayOfTheWeek2(day, month, year))

