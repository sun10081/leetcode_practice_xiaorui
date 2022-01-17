# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2022/1/9 10:29 上午
@desc: 
"""
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0
        for i in range(1, n):
            if nums[i] == 0:
                index = i
                break
        nums_a = nums[index:] + nums[:index]
        ans = min(self._minSwaps(nums), self._minSwaps(nums_a))
        return ans

    def _minSwaps(self, data: List[int]) -> int:
        x = data.count(1)
        n = len(data)
        sm = 0
        for i in range(x):
            if data[i] == 1:
                sm += 1
        res = sm
        for i in range(x, n):
            if data[i] == 1:
                sm += 1
            if data[i - x] == 1:
                sm -= 1
            res = max(res, sm)
        return x - res


class Solution2:
    def minSwaps(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    nums = [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1,
            0, 1, 1, 0, 1, 1]
    s = Solution()
    print(s.minSwaps(nums))
