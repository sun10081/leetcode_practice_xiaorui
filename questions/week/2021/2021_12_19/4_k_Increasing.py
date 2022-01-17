# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 4_k_Increasing
@time: 2021/12/19 11:35 上午
@desc: 
"""
import bisect
from bisect import bisect_right
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            sub = arr[i::k]
            lis = []
            for num in sub:
                if not lis or lis[-1] <= num:
                    lis.append(num)
                else:
                    loc = bisect.bisect_right(lis, num)
                    lis[loc] = num
            ans += len(sub) - len(lis)
        return ans

    def kIncreasing2(self, arr: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            sub = arr[i::k]
            lis = []
            for x in sub:
                if not lis or lis[-1] <= x:
                    lis.append(x)
                else:
                    loc = bisect_right(lis, x)
                    lis[loc] = x
            ans += len(sub) - len(lis)
        return ans


if __name__ == '__main__':
    arr = [12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3]
    k = 1
    # arr = [4, 1, 5, 2, 6, 2]
    # k = 3
    s = Solution()
    print(s.kIncreasing2(arr, k))
