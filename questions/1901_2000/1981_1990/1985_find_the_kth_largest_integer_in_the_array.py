# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1985_find_the_kth_largest_integer_in_the_array.py
@time: 2022-01-15 20:44:24 
"""
from typing import List
from functools import cmp_to_key

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def quick_select(l: int, r: int, k: int) -> str:
            if l == r:
                return nums[l]
            i, j = l - 1, r + 1
            x = int(nums[(l + r) >> 1])
            while i < j:
                i += 1
                while int(nums[i]) < x:
                    i += 1
                j -= 1
                while int(nums[j]) > x:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            # 计算数量 + 1
            sl = j - l + 1
            if k <= sl:
                return quick_select(l, j, k)
            # 右区间 减去sl的数量才是排名
            return quick_select(j + 1, r, k - sl)

        n = len(nums)
        # 升序数组，所以需要转化下k排名
        return quick_select(0, n - 1, n - k + 1)

    def kthLargestNumber2(self, nums: List[str], k: int) -> str:
        nums.sort(key=cmp_to_key(lambda x, y: int(x) - int(y)))
        n = len(nums)
        return nums[n - k]


if __name__ == '__main__':
    nums = ["2","21","12","1"]
    k = 3
    s = Solution()
    print(s.kthLargestNumber2(nums, k))
    print(nums)

