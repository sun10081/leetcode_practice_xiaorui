# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 475_heaters
@time: 2021/12/20 9:50 上午
@desc: 
"""
import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            # 二分找到离屋子最近的两供暖器
            right = bisect.bisect_right(heaters, house)
            left = right - 1
            # 边界情况
            right_distance = heaters[right] - house if right < len(heaters) else float("inf")
            left_distance = house - heaters[left] if left >= 0 else float("inf")
            # 取最短距离
            distance = min(left_distance, right_distance)
            ans = max(ans, distance)
        return ans


class Solution2:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            right = bisect.bisect_right(heaters, house)
            left = right - 1
            right_distance = heaters[right] - house if right < len(heaters) else float("inf")
            left_distance = house - heaters[left] if left >= 0 else float("inf")
            distance = min(left_distance, right_distance)
            ans = max(ans, distance)
        return ans


if __name__ == '__main__':
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    s = Solution2()
    print(s.findRadius(houses, heaters))
