# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 77_combine
@time: 2021/12/10 4:40 下午
@desc: 
"""
import datetime
from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(begin: int):
            if len(sequence) == k:
                ans.append(sequence[:])
                return

            upper = n + 1 - (k - len(sequence)) + 1
            for i in range(begin, upper):
                sequence.append(i)
                # print(sequence)
                dfs(i + 1)
                sequence.pop()
                # print(sequence)

        ans = []
        if n < k:
            return ans
        sequence = []
        dfs(1)
        return ans

    def combine2(self, n: int, k: int) -> List[List[int]]:
        # 直接调用库函数
        return [list(tmp) for tmp in itertools.combinations(range(1, n + 1), k)]


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(begin_index: int):
            if len(sequence) == k:
                ans.append(sequence[:])
                return
            # 搜索起点的上界 = n - (k - path.size()) + 1
            upper = n + 1 - (k - len(sequence)) + 1
            for i in range(begin_index, upper):
                sequence.append(i)
                dfs(i + 1)
                sequence.pop()

        ans = []
        if n < k:
            return ans
        sequence = []
        dfs(1)
        return ans

    def combine2(self, n: int, k: int) -> List[List[int]]:
        # 直接调用库函数
        return [list(array) for array in itertools.combinations(range(1, n + 1), k)]


class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(being_index: int):
            if len(sequence) == k:
                ans.append(sequence[:])
                return
            # 搜索起点的上界 = n - (k - path.size()) + 1
            upper = n + 1 - (k - len(sequence)) + 1
            for i in range(being_index, upper):
                sequence.append(i)
                dfs(i + 1)
                sequence.pop()

        ans = []
        sequence = []
        dfs(1)
        return ans


if __name__ == '__main__':
    n = 4
    k = 2
    s = Solution3()
    time1 = datetime.datetime.now()
    print(s.combine(n, k))
    time2 = datetime.datetime.now()
    print(f"耗时: {time2 - time1}")
