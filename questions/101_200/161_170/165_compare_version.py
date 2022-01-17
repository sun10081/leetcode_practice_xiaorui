# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 165_compare_version
@time: 2021/12/13 2:15 下午
@desc: 
"""
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else - 1
        return 0

    def compareVersion2(self, version1: str, version2: str) -> int:
        # 忽略前导0，比较大小，长度不一致时的补0处理
        v1_len, v2_len = len(version1), len(version2)
        v1_point, v2_point = 0, 0
        while v1_point < v1_len or v2_point < v2_len:
            x = 0
            while v1_point < v1_len and version1[v1_point] != '.':
                x = 10 * x + int(version1[v1_point])
                v1_point += 1
            # 跳过'.'
            v1_point += 1
            y = 0
            while v2_point < v2_len and version2[v2_point] != '.':
                y = 10 * y + int(version2[v2_point])
                v2_point += 1
            v2_point += 1
            if x != y:
                return 1 if x > y else - 1
        return 0


class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        version_array = list(zip_longest(version1.split('.'), version2.split('.'), fillvalue=0))
        for v1, v2 in version_array:
            if int(v1) != int(v2):
                return 1 if int(v1) > int(v2) else -1
        return 0

    def compareVersion2(self, version1: str, version2: str) -> int:
        version1_len, version2_len = len(version1), len(version2)
        version1_point, version2_point = 0, 0
        while version1_point < version1_len or version2_point < version2_len:
            x = 0
            while version1_point < version1_len and version1[version1_point] != '.':
                x = x * 10 + int(version1[version1_point])
                version1_point += 1
            # 跳过 '.'
            version1_point += 1

            y = 0
            while version2_point < version2_len and version2[version2_point] != '.':
                y = y * 10 + int(version2[version2_point])
                version2_point += 1
            # 跳过 '.'
            version2_point += 1

            if x != y:
                return 1 if x > y else -1
        return 0


if __name__ == '__main__':
    # bad case 11.1.0 / 8.1.0
    # 1.0 / 1.0.0
    # 1.0.1 / 1
    # 7.5.2.4 / 7.5.3
    # 2.20.3 / 2.1.4
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    s = Solution2()
    print(s.compareVersion2(version1, version2))
