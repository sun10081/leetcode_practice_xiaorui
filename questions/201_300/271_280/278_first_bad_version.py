# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 278_first_bad_version
@time: 2021/12/13 12:24 上午
@desc: 
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid
        return left

    def isBadVersion(self, version: int) -> bool:
        pass

    def firstBadVersion2(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left + 1) // 2
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def firstBadVersion3(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if not self.isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left



