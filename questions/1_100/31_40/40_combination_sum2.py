# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 40_combination_sum2
@time: 2021/12/9 3:51 下午
@desc: 
"""
import bisect
import datetime
import itertools
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(reset: int, pos: int):
            if reset == 0:
                ans.append(sequence[:])
                return
            if pos == len(candidates):
                return
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                if reset - candidates[i] >= 0:
                    sequence.append(candidates[i])
                    dfs(reset - candidates[i], i + 1)
                    sequence.pop()

        candidates.sort()
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
            if begin_index == len(candidates):
                return

            for i in range(begin_index, len(candidates)):
                if i > begin_index and candidates[i] == candidates[i - 1]:
                    continue
                # if surplus - candidates[begin_index] < 0:
                #     break
                if surplus - candidates[i] >= 0:
                    sequence.append(candidates[i])
                    dfs(surplus - candidates[i], i + 1)
                    sequence.pop()

        ans = []
        sequence = []
        candidates.sort()
        dfs(target, 0)
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        for i in range(1, len(candidates)):
            for array in itertools.combinations(candidates, i):
                if sum(array) == target and list(array) not in ans:
                    ans.append(list(array))
        return ans if not (len(candidates) == 1 and candidates[0] == target) else [candidates]


class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(surplus: int, begin_index: int):
            if surplus == 0:
                ans.append(sequence[:])
                # print(sequence)
                return
            if surplus < 0 or begin_index == n:
                return

            for i in range(begin_index, n):
                if surplus - candidates[i] >= 0:
                    if i > begin_index and candidates[i] == candidates[i - 1]:
                        continue
                    sequence.append(candidates[i])
                    dfs(surplus - candidates[i], i + 1)
                    sequence.pop()

        ans = []
        sequence = []
        n = len(candidates)
        candidates.sort()
        dfs(target, 0)
        # print(len(ans))
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 会超时
        ans = []
        candidates.sort()
        left = bisect.bisect(candidates, target)
        candidates = candidates[:left]
        for i in range(0, len(candidates)):
            if candidates[i] > target:
                break
            tmp_set = set(itertools.combinations(candidates, i + 1))
            for sequence in tmp_set:
                if sum(sequence) == target:
                    ans.append(list(sequence))
                    print(len(ans))
        return ans


if __name__ == '__main__':
    candidates = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21,
                  29, 24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34,
                  18, 12]
    target = 27
    s = Solution3()
    time1 = datetime.datetime.now()
    print(s.combinationSum(candidates, target))
    time2 = datetime.datetime.now()
    print(f"耗时: {time2 - time1}")
