# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 567_check_inclusion
@time: 2021/12/17 4:39 下午
@desc: 
"""
import copy
from itertools import permutations
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 一行流 超时
        return any([True if "".join(s) in s2 else False for s in permutations(s1)])

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        def check(s: str, l: int, r: int) -> bool:
            tmp_counts = copy.deepcopy(counts)
            for ch in s[l:r]:
                idx = ord(ch) - ord("a")
                if tmp_counts[idx] == 0:
                    return False
                else:
                    tmp_counts[idx] -= 1
            return True if not any(tmp_counts) else False

        if len(s2) < len(s1):
            return False
        counts = [0] * 26
        for ch in s1:
            index = ord(ch) - ord("a")
            counts[index] += 1
        left, right = 0, 0
        while right < len(s2):
            right_index = ord(s2[right]) - ord("a")
            if counts[right_index] != 0:
                left = right
                while counts[right_index] != 0:
                    right += 1
                if right - left != len(s1):
                    right += 1
                    continue
                else:
                    res = check(s2[left: right], left, right)
                    if res:
                        return True
            right += 1
        return False

    def checkInclusion3(self, s1: str, s2: str) -> bool:
        def check(s: str, l: int, r: int) -> bool:
            tmp_counts = copy.deepcopy(counts)
            for ch in s[l:r]:
                idx = ord(ch) - ord("a")
                if tmp_counts[idx] == 0:
                    return False
                else:
                    tmp_counts[idx] -= 1
            return True if not any(tmp_counts) else False

        if len(s2) < len(s1):
            return False
        counts = [0] * 26
        for ch in s1:
            index = ord(ch) - ord("a")
            counts[index] += 1
        left, right = 0, len(s1) - 1
        if check(s2, left, right + 1):
            return True
        while right < len(s2):
            right_index = ord(s2[right]) - ord("a")
            # left_index = ord(s2[left]) - ord("a")
            if counts[right_index] != 0:
                res = check(s2, left, right + 1)
                if res:
                    return True
            right += 1
            left += 1
        return False

    def checkInclusion4(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if n < m:
            return False
        count = [0] * 26
        for i in range(m):
            count[ord(s1[i]) - ord("a")] -= 1
            count[ord(s2[i]) - ord("a")] += 1
        diff = 0
        for cnt in count:
            if cnt:
                diff += 1
        if diff == 0:
            return True
        for i in range(m, n):
            x = ord(s2[i]) - ord("a")
            y = ord(s2[i - m]) - ord("a")
            if x == y:
                continue
            if count[x] == 0:
                diff += 1
            count[x] += 1
            if count[x] == 0:
                diff -= 1

            if count[y] == 0:
                diff += 1
            count[y] -= 1
            if count[y] == 0:
                diff -= 1
            if diff == 0:
                return True
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaoo"

    s = Solution()
    print(s.checkInclusion4(s1, s2))
