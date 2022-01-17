# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 39_combination_sum
@time: 2021/12/9 4:08 下午
@desc: 
"""
import datetime
import itertools
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(reset: int, pos: int):
            if reset == 0:
                ans.append(sequence[:])
                return
            if pos == len(candidates):
                return
            # 跳过当前数
            dfs(reset, pos + 1)
            # 选择当前数
            if reset - candidates[pos] >= 0:
                sequence.append(candidates[pos])
                # print(f"递归之前 {sequence}, 剩余{reset - candidates[pos]}")
                dfs(reset - candidates[pos], pos)
                sequence.pop()
                # print(f"递归之后 {sequence}")

        ans = []
        sequence = []
        dfs(target, 0)
        return ans


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(surplus: int, begin_index: int):
            if surplus == 0:
                ans.append(sequence[:])
                return
            if surplus < 0 or begin_index == len(candidates):
                return

            dfs(surplus, begin_index + 1)

            if surplus - candidates[begin_index] >= 0:
                sequence.append(candidates[begin_index])
                dfs(surplus - candidates[begin_index], begin_index)
                sequence.pop()

        ans = []
        sequence = []
        dfs(target, 0)
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        for i in range(1, target // candidates[0] + 1):
            for array in itertools.combinations_with_replacement(candidates, i):
                if sum(array) == target:
                    ans.append(list(array))
        return ans


class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(surplus: int, begin_index: int):
            if surplus == 0:
                ans.append(sequence[:])
                return
            if surplus < 0 or begin_index == n:
                return
            dfs(surplus, begin_index + 1)
            if surplus - candidates[begin_index] >= 0:
                sequence.append(candidates[begin_index])
                print(sequence)
                dfs(surplus - candidates[begin_index], begin_index)
                sequence.pop()
                print(sequence)

        ans = []
        sequence = []
        n = len(candidates)
        dfs(target, 0)
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        for i in range(1, target // candidates[0] + 1):
            for sequence in itertools.combinations_with_replacement(candidates, i):
                if sum(sequence) == target:
                    ans.append(list(sequence))
        return ans


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    s = Solution3()
    time1 = datetime.datetime.now()
    print(s.combinationSum2(candidates, target))
    time2 = datetime.datetime.now()
    print(f"耗时: {time2 - time1}")
