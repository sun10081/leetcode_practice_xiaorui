# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2022/1/8 10:16 下午
@desc: 
"""
from typing import Optional
from questions.public import ListNode

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        left = head
        right = head
        n = 0
        while left:
            ans.append(left.value)
            left = left.next
            n += 1
        for i in range(n // 2):
            ans[i] += ans[n - 1 - i]
        return max(ans[:n//2])




