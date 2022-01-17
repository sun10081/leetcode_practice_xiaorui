# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3_getDistances
@time: 2021/12/26 4:45 下午
@desc: 
"""
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            # index, value, ans
            arr[i] = [i, arr[i], 0]
        arr.sort(key=lambda x: x[1])
        for i in range(n):
            distance = 0
            point = i - 1
            while point >= 0 and arr[i][1] == arr[point][1]:
                distance += abs(arr[i][0] - arr[point][0])
                point -= 1

            point = i + 1
            while point < n and arr[i][1] == arr[point][1]:
                distance += abs(arr[i][0] - arr[point][0])
                point += 1
            arr[i][2] = distance

        res = []
        arr.sort(key=lambda x: x[0])
        for i in range(n):
            res.append(arr[i][2])
        return res


if __name__ == '__main__':
    arr = [10,5,10,10]
    s = Solution()
    print(s.getDistances(arr))


