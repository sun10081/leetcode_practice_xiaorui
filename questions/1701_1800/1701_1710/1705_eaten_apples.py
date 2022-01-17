# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1705_eaten_apples
@time: 2021/12/24 10:02 上午
@desc: 
"""
import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        apple_list = []
        n = len(apples)
        for i in range(n):
            apple_list.append([apples[i], i + 1, i + days[i]])
        apple_list.sort(key=lambda x: x[2])
        eaten_apples = 0
        cur_day = 1
        while apple_list:
            seq = []
            index_count = 0
            for i in range(len(apple_list)):
                if apple_list[i][0] > 0 and apple_list[i][1] <= cur_day <= apple_list[i][2]:
                    eaten_apples += 1
                    apple_list[i][0] -= 1
                    break
                if apple_list[i][0] <= 0 or cur_day > apple_list[i][2]:
                    seq.append(i)
            for num in seq:
                apple_list.pop(num - index_count)
                index_count += 1

            cur_day += 1

        return eaten_apples


class Solution2:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        eaten_apples = 0
        cur_day = 0
        apple_list = []
        while cur_day < len(apples):
            while apple_list and apple_list[0][0] <= cur_day:
                heapq.heappop(apple_list)
            if apples[cur_day]:
                heapq.heappush(apple_list, [cur_day + days[cur_day], apples[cur_day]])
            # 极端情况 如 apples = [3,0,0,0,0,2]
            if apple_list:
                apple_list[0][1] -= 1
                eaten_apples += 1
                if apple_list[0][1] == 0:
                    heapq.heappop(apple_list)
            cur_day += 1

        while apple_list:
            while apple_list and apple_list[0][0] <= cur_day:
                heapq.heappop(apple_list)
            if not apple_list:
                break
            if apple_list[0][1]:
                apple_list[0][1] -= 1
                eaten_apples += 1
                if apple_list[0][1] == 0:
                    heapq.heappop(apple_list)
            cur_day += 1
        return eaten_apples


class Solution3:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        eaten_apples = 0
        cur_day = 0
        apple_list = []
        # 有新增苹果时
        while cur_day < len(apples):
            # 过期苹果 直接排除
            while apple_list and apple_list[0][0] <= cur_day:
                heapq.heappop(apple_list)
            # 苹果数量不为0 加入堆中
            if apples[cur_day]:
                heapq.heappush(apple_list, [cur_day + days[cur_day], apples[cur_day]])
            # 吃苹果
            if apple_list:
                apple_list[0][1] -= 1
                eaten_apples += 1
                # 数量为0 排除
                if apple_list[0][1] == 0:
                    heapq.heappop(apple_list)
            cur_day += 1
        # 无新增苹果时
        while apple_list:
            # 过期苹果 直接排除
            while apple_list and apple_list[0][0] <= cur_day:
                heapq.heappop(apple_list)
            # 堆中无苹果 结束循环
            if not apple_list:
                break
            if apple_list[0][1]:
                apple_list[0][1] -= 1
                eaten_apples += 1
                # 数量为0 排除
                if apple_list[0][1] == 0:
                    heapq.heappop(apple_list)
            cur_day += 1
        return eaten_apples


if __name__ == '__main__':
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    s = Solution3()
    print(s.eatenApples(apples, days))
