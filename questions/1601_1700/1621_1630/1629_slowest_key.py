# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1629_slowest_key
@time: 2022/1/9 12:52 上午
@desc: 
"""
from typing import List
from collections import defaultdict


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # 时间On， 空间O(26)，其实不需要dict的
        count = defaultdict(int)
        ans = keysPressed[0]
        count[ans] = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            count[keysPressed[i]] = max(count[keysPressed[i]], releaseTimes[i] - releaseTimes[i - 1])
            if count[keysPressed[i]] > count[ans]:
                ans = keysPressed[i]
            if count[keysPressed[i]] == count[ans] and keysPressed[i] > ans:
                ans = keysPressed[i]
        return ans


class Solution2:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        max_time = releaseTimes[0]
        max_key = keysPressed[0]
        for i in range(1, n):
            time = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]
            if time > max_time:
                max_time = time
                max_key = key
            elif time == max_time:
                if key > max_key:
                    max_time = time
                    max_key = key
        return max_key


if __name__ == '__main__':
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"
    s = Solution()
    print(s.slowestKey(releaseTimes, keysPressed))
