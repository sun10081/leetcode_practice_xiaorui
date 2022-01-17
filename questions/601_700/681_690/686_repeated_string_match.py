# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 686_repeated_string_match
@time: 2021/12/22 12:11 上午
@desc: 
"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        elif b == '':
            return 0

        repeat_count = 1
        m, n = len(a), len(b)
        point_a, point_b = 0, 0
        while point_a < m and a[point_a] != b[point_b]:
            point_a += 1
        if point_a == m:
            return -1
        while point_b < n:
            if point_a == m:
                point_a = 0
                repeat_count += 1
            if a[point_a] == b[point_b]:
                point_a += 1
                point_b += 1
            elif a[point_a] != b[point_b]:
                return -1
        return repeat_count

    def repeatedStringMatch2(self, a: str, b: str) -> int:
        if b in a:
            return 1
        elif b == '':
            return 0
        # repeat_count = 1
        m, n = len(a), len(b)
        need_repeat = n // m + 2
        for i in range(2, need_repeat + 1):
            tmp_a = a * i
            if b in tmp_a:
                return i
        return -1


class Solution2:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        elif b == '':
            return 0

        m, n = len(a), len(b)
        repeat_count = n // m + 2
        for i in range(1, repeat_count + 1):
            tmp_a = a * i
            if b in tmp_a:
                return i
        return -1

    def repeatedStringMatch2(self, a: str, b: str) -> int:
        # if b in a:
        #     return 1
        # elif b == '':
        #     return 0

        m, n = len(a), len(b)
        repeat_count = n // m + 2
        tmp_a = a * repeat_count
        index = tmp_a.find(b)
        if index == -1:
            return -1
        return 1 + (index + n - 1) // m


class Solution3:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        if b == '':
            return 0

        m, n = len(a), len(b)
        repeat_count = n // m + 2
        tmp_a = a * repeat_count
        index = tmp_a.find(b)
        if tmp_a.find(b) == -1:
            return -1
        # index 为起始坐标，n - 1为字符串b的坐标长度，
        # 相加即为字符串b的结束坐标，整除m的长度 + 1即为重复次数
        return 1 + (index + n - 1) // m


if __name__ == '__main__':
    a = "abcd"
    b = "cdabcdab"
    # print(a * 2)
    s = Solution3()
    print(s.repeatedStringMatch(a, b))
