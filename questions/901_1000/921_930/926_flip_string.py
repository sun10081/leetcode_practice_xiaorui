# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 926_flip_string.py
@time: 2023-11-10 14:38:50 
"""
from typing import List


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # 前缀和
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + int(s[i - 1])
        # 最差情况 把1全部变成0
        ans = n - pre_sum[n]
        # 枚举分界点 左侧0 右侧1
        for i in range(1, n + 1):
            # 左侧1的数量 需要翻转变成0
            one_cnt = pre_sum[i]
            # 右侧0的数量 需要翻转变成1
            zero_cnt = n - i - (pre_sum[n] - pre_sum[i])
            ans = min(ans, one_cnt + zero_cnt)
        return ans


if __name__ == '__main__':
    so = Solution()
    s = "0101100011"
    print(so.minFlipsMonoIncr(s))
