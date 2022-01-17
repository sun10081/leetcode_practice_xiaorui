"""
@author: guoxiaorui
@file: 786_kth_smallest_prime_fraction.py
@time: 2021/11/29 10:10 上午
@desc: 
"""
import heapq
from typing import List, Tuple
from functools import cmp_to_key
from heapq import *


class Solution:
    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:
        """
        纯暴力
        :param arr:
        :param k:
        :return:
        """
        n = len(arr)
        frac = list()
        for i in range(n):
            for j in range(i + 1, n):
                frac.append((arr[i], arr[j], arr[i] / arr[j]))

        frac.sort(key=lambda x: x[2])
        return list(frac[k - 1][0:2])

    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        """
        自定义排序 a/b > c/d ==>  a * d > b * c
        :param arr:
        :param k:
        :return:
        """

        def cmp(x: Tuple[int, int], y: Tuple[int, int]) -> int:
            return -1 if x[0] * y[1] < x[1] * y[0] else 1

        n = len(arr)
        frac = list()
        for i in range(n):
            for j in range(i + 1, n):
                frac.append((arr[i], arr[j]))

        frac.sort(key=cmp_to_key(cmp))
        return list(frac[k - 1])

    def kthSmallestPrimeFraction3(self, arr: List[int], k: int) -> List[int]:
        """
        优先队列
        :param arr:
        :param k:
        :return:
        """
        pass


class Solution2:
    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                ans.append([arr[i], arr[j], arr[i] / arr[j]])
        ans.sort(key=lambda x: x[2])
        return ans[k - 1][0:2]

    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        def cmp(x: Tuple[int, int], y: Tuple[int, int]) -> int:
            return -1 if x[0] * y[1] < x[1] * y[0] else 1

        ans = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                ans.append((arr[i], arr[j]))
        ans.sort(key=cmp_to_key(cmp))
        return list(ans[k - 1])


class Frac:
    def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y

    def __lt__(self, other: "Frac") -> bool:
        # python默认为小根堆，这里只需要重写这个方法即可
        return self.x * other.y < self.y * other.x


class Solution3:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # 自定义排序
        def cmp(x: Tuple[int, int], y: Tuple[int, int]) -> int:
            return -1 if x[0] * y[1] < x[1] * y[0] else 1

        ans = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                ans.append((arr[i], arr[j]))
        ans.sort(key=cmp_to_key(cmp))
        print(ans)
        return list(ans[k - 1])

    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:
        ans = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                ans.append((arr[i], arr[j]))
        # 自定义排序
        ans.sort(key=cmp_to_key(lambda x, y: x[0] * y[1] - x[1] * y[0]))
        print(ans)
        return list(ans[k - 1])

    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        ans = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapq.heapify(ans)
        # 进行k - 1次pop，堆顶元素即为所求
        for _ in range(k - 1):
            frac = heapq.heappop(ans)
            i, j = frac.idx, frac.idy
            # arr为有序数组，分子坐标大于分母，没有比较的意义，所以i的上界就是j，遍历i就要看i+1的值是否比j小
            if i + 1 < j:
                heapq.heappush(ans, Frac(i + 1, j, arr[i + 1], arr[j]))
        return [ans[0].x, ans[0].y]


if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    k = 3
    s = Solution3()
    print(s.kthSmallestPrimeFraction2(arr, k))
