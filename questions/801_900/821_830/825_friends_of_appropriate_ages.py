# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 825_friends_of_appropriate_ages
@time: 2021/12/27 10:21 上午
@desc: 
"""
import bisect
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        排序 + 二分
        :param ages:
        :return:
        """
        n = len(ages)
        ages.sort()
        ans = 0
        left, right = 0, 0
        for i in range(n):
            if ages[i] <= 14:
                continue
            lower = 0.5 * ages[i] + 7
            left = bisect.bisect_right(ages, lower, lo=left)
            right = bisect.bisect_right(ages, ages[i], lo=right) - 1
            # 坐标计算个数，做差要+1，排除ages[i]本身，要-1 刚好抵消
            ans += right - left
        return ans

    def numFriendRequests2(self, ages: List[int]) -> int:
        """
        0.5 * ages[x] + 7 < ages[y] <= ages[x]
        排序 + 双指针
        :param ages:
        :return:
        """
        n = len(ages)
        ages.sort()
        ans = 0
        left, right = 0, 0
        for i in range(n):
            if ages[i] <= 14:
                continue
            lower = 0.5 * ages[i] + 7
            while ages[left] <= lower:
                left += 1
            while right < n and ages[right] <= ages[i]:
                right += 1
            # 这里 -1 是对应二分法中的-1处理，即找到刚比ages[i]大的元素，
            # 它的上一个元素就是value == ages[i]的最后一个元素
            ans += (right - 1) - left
        return ans


if __name__ == '__main__':
    ages = [20, 30, 100, 110, 120]
    s = Solution()
    print(s.numFriendRequests2(ages))
