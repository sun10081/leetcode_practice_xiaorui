# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2_good_days_to_rob_bank
@time: 2021/12/11 11:08 下午
@desc: 
"""
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if len(security) < time * 2 + 1:
            return []
        ans = []
        for i in range(time, len(security) - time):
            if self.valid_day(security, time, i):
                ans.append(i)
        return ans

    def valid_day(self, security: List[int], time: int, index: int) -> bool:
        if index - time < 0 or index + time > len(security) - 1:
            return False
        for i in range(index - time, index):
            if security[i] < security[i + 1]:
                return False
        for i in range(index, index + time):
            if security[i] > security[i + 1]:
                return False
        return True


class Solution2:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if len(security) < time * 2 + 1:
            return []
        ans = []

        # 递增
        valid1 = [False] * (len(security) - 1)
        # 递减
        valid2 = [False] * (len(security) - 1)
        for i in range(len(security) - 1):
            if security[i] >= security[i + 1]:
                valid1[i] = True
            if security[i] <= security[i + 1]:
                valid2[i] = True
        for i in range(time, len(security) - time):
            for j in range(time):
                if valid1[i - time + j] and valid2[i + j]:
                    continue
                else:
                    break
            else:
                ans.append(i)
        return ans


class Solution3:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        increase = [0] * n
        decrease = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                decrease[i] = decrease[i - 1] + 1
            else:
                decrease[i] = 0
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
    security = [1, 1, 1, 1, 1]
    time = 0
    s = Solution3()
    print(s.goodDaysToRobBank(security, time))
