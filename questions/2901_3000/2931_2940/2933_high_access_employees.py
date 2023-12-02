# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2933_high_access_employees.py
@time: 2023-11-15 11:11:48 
"""
from typing import List
from collections import defaultdict


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        count = defaultdict(List)
        access_times.sort(key=lambda x: (x[0], x[1]))
        for emp, time in access_times:
            if emp not in count:
                count[emp] = [time]
            else:
                count[emp].append(time)
        ans = []
        for emp, time_list in count.items():
            for i in range(len(time_list) - 2):
                if self.valid_time(time_list[i], time_list[i + 1]) and self.valid_time(time_list[i], time_list[i + 2]):
                    ans.append(emp)
                    break
        return ans

    def valid_time(self, time1: str, time2: str) -> bool:
        if time1.startswith('00') and time1.startswith('23'):
            return False
        hour_diff = int(time2[:2]) - int(time1[:2])
        min_diff = int(time2[2:]) - int(time1[2:])
        time_diff = hour_diff * 60 + min_diff
        return time_diff < 60


class Solution2:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort()
        count = defaultdict(list)
        ans = []
        for emp, time in access_times:
            if emp not in count:
                count[emp] = [time]
            else:
                count[emp].append(time)
        for emp, time_list in count.items():
            for i in range(0, len(time_list) - 2):
                if self.valid_time(time_list[i], time_list[i + 2]):
                    ans.append(emp)
                    break
        return ans

    def valid_time(self, time1: str, time2: str) -> bool:
        if time1.startswith('23') and time2.startswith("00"):
            return False
        hour = (int(time2[:2]) - int(time1[:2])) * 60
        minute = int(time2[2:]) - int(time1[2:])
        return True if hour + minute < 60 else False


if __name__ == '__main__':
    s = Solution2()
    access_times = [["d", "0002"], ["c", "0808"], ["c", "0829"], ["e", "0215"], ["d", "1508"], ["d", "1444"],
                    ["d", "1410"], ["c", "0809"]]
    print(s.findHighAccessEmployees(access_times))
