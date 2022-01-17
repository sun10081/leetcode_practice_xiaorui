# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1_max_subsequence
@time: 2021/12/11 10:32 下午
@desc: 
"""
from typing import List
from collections import defaultdict
import itertools


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # nums.sort()
        ans = []
        max_value = float("-inf")
        tmp_array = [list(array) for array in itertools.combinations(nums, k)]
        for i in tmp_array:
            if max_value < sum(i):
                max_value = sum(i)
                ans = i
        return ans

    def maxSubsequence2(self, nums: List[int], k: int) -> List[int]:
        def dfs(begin_index: int):
            nonlocal max_value, ans
            if len(sequence) == k:
                if max_value < sum(sequence):
                    max_value = sum(sequence)
                    ans = sequence[:]

                return
            # 搜索起点的上界 = n - (k - path.sequence()) + 1
            upper = n - (k - len(sequence)) + 1
            for i in range(begin_index, upper):
                sequence.append(nums[i])
                dfs(i + 1)
                sequence.pop()

        ans = []
        max_value = float("-inf")
        n = len(nums)
        sequence = []
        dfs(0)
        return ans

    def maxSubsequence3(self, nums: List[int], k: int) -> List[int]:
        array = []
        for i, num in enumerate(nums):
            tmp = [num, i]
            array.append(tmp)
        array.sort(key=lambda x: x[0])
        array = array[len(nums) - k:len(nums) + 1]
        ans = []
        array.sort(key=lambda x: x[1])
        for i in range(len(array)):
            ans.append(array[i][0])
        return ans


class Solution2:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        nums.sort(key=lambda x: x[0], reverse=True)
        nums = nums[:k]
        nums.sort(key=lambda x: x[1])
        return [i[0] for i in nums]


if __name__ == '__main__':
    nums = [-76, -694, 44, 197, 357, -833, -277, 358, 724, -585, -960, 214, 465, -593, -431, 625, -83, 58, -889, 31,
            765, 8,
            -17, 476, 992, 803, 863, 242, 379, 561, 673, 526, -447]
    k = 14
    # nums = [1]
    # k = 1
    s = Solution2()
    print(s.maxSubsequence(nums, k))
