# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 907_sum_of_subarray_minimums.py
@time: 2023-11-27 11:09:20 
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack, left = [], [-1] * n
        # 左边界 left[i] 为左侧严格小于 arr[i] 的最近元素位置（不存在时为 -1）
        for i, x in enumerate(arr):
            while stack and x <= arr[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack, right = [], [n] * n
        # 右边界 right[i] 为右侧小于等于 arr[i] 的最近元素位置（不存在时为 n）
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (r - i) * (i - l)
        return ans % (10 ** 9 + 7)

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        n = len(arr)
        stack, left, right = [], [-1] * n, [n] * n
        for i, x in enumerate(arr):
            while stack and x <= arr[stack[-1]]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (r - i) * (i - l)
        return ans % (10 ** 9 + 7)

    def sumSubarrayMins3(self, arr: List[int]) -> int:
        arr.append(-1)
        ans, stack = 0, [-1]
        for r, x in enumerate(arr):
            while len(stack) > 1 and x <= arr[stack[-1]]:
                i = stack.pop()
                ans += arr[i] * (r - i) * (i - stack[-1])
            stack.append(r)
        return ans % (10 ** 9 + 7)






