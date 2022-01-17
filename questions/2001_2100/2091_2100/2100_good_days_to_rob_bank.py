# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2100_good_days_to_rob_bank
@time: 2021/12/14 4:50 下午
@desc: 
"""
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        increase = [0] * n
        decrease = [0] * n
        # 递减 从左向右统计
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                decrease[i] = decrease[i - 1] + 1
            else:
                decrease[i] = 0
        # 递增 从右向左统计
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                increase[i] = increase[i + 1] + 1
            else:
                increase[i] = 0
        # 可以打结银行的条件 time <= increase[i] and time <= decrease[i]
        ans = []
        for i in range(n):
            if time <= increase[i] and time <= decrease[i]:
                ans.append(i)
        return ans


class Solution2:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        increase = [0] * n
        decrease = [0] * n
        # 从左到右 递减
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                decrease[i] = decrease[i - 1] + 1
            else:
                decrease[i] = 0

        # 从右到左 递增
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                increase[i] = increase[i + 1] + 1
            else:
                increase[i] = 0

        ans = []
        for i in range(n):
            if increase[i] >= time and decrease[i] >= time:
                ans.append(i)
        return ans


if __name__ == '__main__':
    security = [5, 3, 3, 3, 5, 6, 2]
    time = 2
    s = Solution2()
    print(s.goodDaysToRobBank(security, time))
